import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Step 1: Create a session and load the page
driver = webdriver.Chrome()
driver.get('https://pubs.rsc.org/en/content/articlelanding/2020/na/d0na00118j')

# Wait for the page to fully load
driver.implicitly_wait(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all('table')

# Step 3: Read tables with Pandas read_html()
dfs = pd.read_html(str(tables))

print(f'Total tables: {len(dfs)}')
print(dfs[0])

driver.close()