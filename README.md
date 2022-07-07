[![View on Medium](https://img.shields.io/badge/Medium-View%20on%20Medium-red?logo=medium)](https://bindichen.medium.com/) [![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/BindiChen/machine-learning)

# Machine Learning
Practical Machine Learning topics for articles in my [Medium blog](https://bindichen.medium.com/) 

#### Content
1. [General Setup](#general-setup)
1. [Data Analysis](#data-analysis)
   * [Pandas](#pandas)
   * [Applied Data Analysis and EDA](#applied-data-analysis-and-eda)
1. [Web scraping](#web-scraping)
1. [Data Visualization](#data-visualization)
1. [TensorFlow](#tensorflow)
1. [PyTorch](#pytorch)
1. [Scikit-Learn](#scikit-learn-and-general-machine-learning)

## General Setup
* [Create Virtual Environment using “virtualenv” and add it to Jupyter Notebook](https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415)
* [Create Virtual Environment using “conda” and add it to Jupyter Notebook](https://medium.com/analytics-vidhya/create-virtual-environment-using-conda-and-add-it-to-jupyter-notebook-d319a81dfd1)
* [7 ways to load external data into Google Colab](https://bindichen.medium.com/7-ways-to-load-external-data-into-google-colab-7ba73e7d5fc7)


## Data Analysis

### Pandas

* Reading & Writing data
    * [4 tricks to parse date columns with Pandas `read_csv()`](https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/012-parse-date-with-read_csv/parse-date-column-with-read_csv.ipynb)
    * [Pandas `read_csv()` tricks you should know](https://medium.com/@bindiatwork/all-the-pandas-read-csv-you-should-know-to-speed-up-your-data-analysis-1e16fe1039f3) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/006-pandas-read_csv/read_csv-tricks.ipynb)
    * [All Pandas `read_html()` you should know for scraping data from HTML tables](https://bindichen.medium.com/all-pandas-read-html-you-should-know-for-scraping-data-from-html-tables-a3cbb5ce8274) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/024-pandas-read_html/pandas-read_html.ipynb)
    * [How to convert JSON into a Pandas DataFrame?](https://bindichen.medium.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/027-pandas-convert-json/pandas-convert-json.ipynb)
    * [Pandas `json_normalize()` for flattening JSON](https://bindichen.medium.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/028-pandas-json_normalize/pandas-json_normalize.ipynb)
* Data Profiling
    * [9 Pandas `value_counts()` tricks](https://towardsdatascience.com/9-pandas-value-counts-tricks-to-improve-your-data-analysis-7980a2b46536) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/046-pandas-value_counts/pandas-value_counts.ipynb)
    * [Getting more value from the Pandas `count()`](https://bindichen.medium.com/getting-more-value-from-the-pandas-count-3e45a62c7077) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/043-pandas-count/pandas-count.ipynb)
* Data Preprocessing
    * [What is One-Hot Encoding and how to use `get_dummies()`](https://towardsdatascience.com/what-is-one-hot-encoding-and-how-to-use-pandas-get-dummies-function-922eb9bd4970) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/002-one-hot-encoding/one-hot-encoding.ipynb)
    * [Working with missing values in Pandas](https://towardsdatascience.com/working-with-missing-values-in-pandas-5da45d16e74) | TBA soon
    * [Working with datetime in Pandas DataFrame](https://towardsdatascience.com/working-with-datetime-in-pandas-dataframe-663f7af6c587) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/008-pandas-datetime/pandas-datetime.ipynb)
    * [11 Tricks to Master `sort_values()` in Pandas](https://bindichen.medium.com/11-tricks-to-master-values-sorting-in-pandas-7f2cfbf19730) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/040-pandas-sort_values/pandas-sort_values.ipynb)
    * [How to do a Custom Sort on Pandas DataFrame](https://bindichen.medium.com/how-to-do-a-custom-sort-on-pandas-dataframe-ac18e7ea5320) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/017-pandas-custom-sort/pandas-custom-sort.ipynb)
    * [Pandas `cut()` to transform numerical data into categorical data](https://bindichen.medium.com/all-pandas-cut-you-should-know-for-transforming-numerical-data-into-categorical-data-1370cf7f4c4f) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/026-pandas-cut/pandas-cut.ipynb)
    * [Pandas `qcut()` for binning numerical data based on sample quantiles](https://bindichen.medium.com/all-pandas-qcut-you-should-know-for-binning-numerical-data-based-on-sample-quantiles-c8b13a8ed844) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/041-pandas-qcut/pandas-qcut.ipynb)
    * [Finding and removing duplicate rows in Pandas DataFrame](https://bindichen.medium.com/finding-and-removing-duplicate-rows-in-pandas-dataframe-c6117668631f) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/034-pandas-find-and-remove-duplicates/pandas-duplicates.ipynb)
    * [Renaming columns in a Pandas DataFrame](https://bindichen.medium.com/renaming-columns-in-a-pandas-dataframe-1d909360ddc6) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/033-pandas-rename-columns/pandas-rename-columns.ipynb)
    * [10 tricks for Converting data to a numeric type](https://bindichen.medium.com/converting-data-to-a-numeric-type-in-pandas-db9415caab0b) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/036-pandas-change-data-to-numeric-type/change-data-to-a-numeric-type.ipynb)
    * [10 tricks for Converting numbers and strings to datetime](https://bindichen.medium.com/10-tricks-for-converting-numbers-and-strings-to-datetime-in-pandas-82a4645fc23d) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/037-pandas-change-data-to-datetime/change-data-to-datetime.ipynb)
    * [Pandas `resample()` tricks for manipulating time-series data](https://bindichen.medium.com/pandas-resample-tricks-you-should-know-for-manipulating-time-series-data-7e9643a7e7f3) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/020-pandas-resample/pandas-resample.ipynb)
    * [When to use Pandas `transform()` function](https://medium.com/@bindiatwork/when-to-use-pandas-transform-function-df8861aa0dcf) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/013-pandas-transform/pandas-transform.ipynb)
    * [Difference between `apply()` and `transform()` in Pandas](https://medium.com/@bindiatwork/difference-between-apply-and-transform-in-pandas-242e5cf32705) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/014-pandas-apply-vs-transform/pandas-apply-vs-transform.ipynb)
    * [Introduction to Pandas `apply()`, `applymap()`, and `map()`](https://towardsdatascience.com/introduction-to-pandas-apply-applymap-and-map-5d3e044e93ff) | TBA soon
    * [All the Pandas `shift()` you should know](https://bindichen.medium.com/all-the-pandas-shift-you-should-know-for-data-analysis-791c1692b5e) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/021-pandas-shift/pandas-shift.ipynb)
    * [Delete rows/columns from a DataFrame using `drop()`](https://bindichen.medium.com/delete-rows-and-columns-from-a-dataframe-using-pandas-drop-d2533cf7b4bd) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/063-pandas-drop/pandas-drop.ipynb)
    * [Flatten MultiIndex columns and rows](https://bindichen.medium.com/how-to-flatten-multiindex-columns-and-rows-in-pandas-f5406c50e569) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/069-pandas-flatten-multiIndex/flatten-multiindex.ipynb)
* Combining data
    * [All the Pandas `merge()` for combining datasets](https://bindichen.medium.com/all-the-pandas-merge-you-should-know-for-combining-datasets-526b9ecaf184) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/018-pandas-merge/pandas-merge.ipynb)
    * [Pandas `concat()` tricks to speed up your data analysis](https://towardsdatascience.com/pandas-concat-tricks-you-should-know-to-speed-up-your-data-analysis-cd3d4fdfe6dd) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/016-pandas-concat/pandas-concat.ipynb)
    * [5 Tricks to master Pandas `append()`](https://bindichen.medium.com/5-tricks-to-master-pandas-append-ede4318cc700) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/055-pandas-append/pandas-append.ipynb)
* Selecting and Querying
    * [Pandas `loc` and `iloc` for selecting data](https://bindichen.medium.com/how-to-use-loc-and-iloc-for-selecting-data-in-pandas-bd09cb4c3d79) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/030-pandas-loc-and-iloc/pandas-loc-and-iloc.ipynb)
    * [Pandas Equivalents of various SQL queries](https://towardsdatascience.com/introduction-to-pandas-equivalents-of-various-sql-queries-448fb57dd9b9) | TBA soon
    * [Creating conditional columns with Numpy `select()` and `where()` methods](https://bindichen.medium.com/creating-conditional-columns-on-pandas-with-numpy-select-and-where-methods-8ee6e2dbd5d5) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/015-pandas-numpy-select-where/pandas-and-numpy-select-where.ipynb)
    * [Accessing data in a MultiIndex DataFrame](https://bindichen.medium.com/accessing-data-in-a-multiindex-dataframe-in-pandas-569e8767201d) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/031-pandas-multiIndex/multiindex-selection.ipynb)
* Reshaping
    * [Reshaping a DataFrame from wide to long format using `melt()`](https://bindichen.medium.com/reshaping-a-dataframe-using-pandas-melt-83a151ce1907) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/048-pandas-melt/pandas-melt.ipynb)
    * [Reshaping a DataFrame from long to wide format using `pivot()`](https://bindichen.medium.com/reshaping-a-dataframe-from-long-to-wide-format-using-pivot-b099930b30ae) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/049-pandas-pivot/pivot.ipynb)
    * [Reshaping a DataFrame/Series with `stack()` and `unstack()`](https://bindichen.medium.com/reshaping-a-dataframe-with-pandas-stack-and-unstack-925dc9ce1289) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/067-pandas-stack/pandas-stack-unstack.ipynb)
* Grouping and Summarizing
    * [Pandas `groupby()` for grouping data and performing operations](https://bindichen.medium.com/all-pandas-groupby-you-should-know-for-grouping-data-and-performing-operations-2a8ec1327b5) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/032-pandas-groupby/pandas-groupby.ipynb)
    * [A Practical Introduction to Pandas `pivot_table()`](https://medium.com/@bindiatwork/a-practical-introduction-to-pandas-pivot-table-function-3e1002dcd4eb) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/003-pandas-pivot-table/003-pandas-pivot-table.ipynb)
    * [Summarizing data with Pandas `crosstab()`](https://bindichen.medium.com/summarizing-data-with-pandas-crosstab-efc8b9abecf) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/045-pandas-crosstab/pandas-crosstab.ipynb)
* Best Practice & Code Readability
    * [Using Pandas `pipe()` to improve code readability](https://towardsdatascience.com/using-pandas-pipe-function-to-improve-code-readability-96d66abfaf8) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/001-pandad-pipe-function/pandas-pipe-to-improve-code-readability.ipynb)
    * [Using Pandas method chaining to improve code readability](https://medium.com/@bindiatwork/using-pandas-method-chaining-to-improve-code-readability-d8517c5626ac) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/007-method-chaining/method-chaining.ipynb)
    * [7 setups you should include at the beginning of a data science project](https://medium.com/@bindiatwork/7-setups-you-should-include-at-the-beginning-of-a-data-science-project-8232ab10a1ec) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/004-7-setups-for-a-data-science-project/7-setups.ipynb)
    * [6 Pandas Tricks you should know to speed up your data analysis](https://towardsdatascience.com/6-pandas-tricks-you-should-know-to-speed-up-your-data-analysis-d3dec7c29e5) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/005-6-pandas-tricks/6-pandas-tricks.ipynb)
    * [8 Commonly used Pandas display options you should know](https://bindichen.medium.com/8-commonly-used-pandas-display-options-you-should-know-a832365efa95) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/035-pandas-display-opts/pandas-display-options.ipynb)
* Introduction & Others
    * [A Practical Introduction to Pandas Series](https://bindichen.medium.com/a-practical-introduction-to-pandas-series-9915521cdc69) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-analysis/029-pandas-series/intro-to-pands-series.ipynb)

### Applied Data Analysis and EDA

* [COVID-19 data processing with Pandas DataFrame](https://towardsdatascience.com/covid-19-data-processing-58aaa3663f6) | TBA soon

## Web scraping
* [Scraping tables from a JavaScript webpage using Selenium, BeautifulSoup, and Pandas](https://medium.com/analytics-vidhya/scraping-tables-from-a-javascript-webpage-using-selenium-beautifulsoup-and-pandas-cbd305ca75fe) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](web-scraping/001-selenium-beautifulSoup-and-pandas/main.py)


## Data Visualization

* [Dual-axis combo chart in Python - Matplotlib, Seaborn, and Pandas `plot()`](https://bindichen.medium.com/creating-a-dual-axis-combo-chart-in-python-52624b187834) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-visualization/0006-dual-axis-combo-chart/dual-axis-combo-chart.ipynb)
* [Adding 3rd Y-axis to combo chart in Python - Matplotlib, Seaborn, and Pandas `plot()`](https://bindichen.medium.com/adding-a-third-y-axis-to-python-combo-chart-39f60fb66708) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-visualization/0010-multiple-y-axis/multiple-y-axis-combo-chart.ipynb)

Altair
* [Python Interactive Data Visualization with Altair](https://towardsdatascience.com/python-interactive-data-visualization-with-altair-b4c4664308f8) | [Gist](https://gist.github.com/BindiChen/0dea2e7fa189f8ff1397180f3b764cc7#file-altair-interactive-selection-chart-py)
* [Interactive Data Visualization for exploring Coronavirus Spreads](https://towardsdatascience.com/interactive-data-visualization-for-exploring-coronavirus-spreads-f33cabc64043) | [Gist](https://gist.github.com/BindiChen/de39182e050962c0b627d5146e3bce09#file-altair-data-visualization-py)

Matplotlib
* [Matplotlib animation in Jupyter Notebook](https://bindichen.medium.com/matplotlib-animations-in-jupyter-notebook-4422e4f0e389) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-visualization/0001-matplotlib-animation/matplotlib-animation-notebook.ipynb)
* [Matplotlib Linear Regression animation in Jupyter Notebook](https://bindichen.medium.com/matplotlib-linear-regression-animation-in-jupyter-notebook-2435b711bea2) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](data-visualization/0002-matplotlib-animation-with-regression/matplotlib-linear-regression-animation.ipynb)

## TensorFlow

* [The Google's 7 steps of Machine Learing in Practice](https://towardsdatascience.com/the-googles-7-steps-of-machine-learning-in-practice-a-tensorflow-example-for-structured-data-96ccbb707d77) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](/tensorflow2/001-googles-7-steps-of-machine-learning-in-practice/001-googles-7-steps-of-machine-learning-in-practice.ipynb)
* [3 ways to create a Machine Learning model with Keras and TensorFlow 2.0](https://towardsdatascience.com/3-ways-to-create-a-machine-learning-model-with-keras-and-tensorflow-2-0-de09323af4d3) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/002-3-ways-to-build-machine-learning-model-with-keras/3-ways-to-build-a-machine-learning-model-with-keras.ipynb)
* [Model Regularization in practice](https://towardsdatascience.com/machine-learning-model-regularization-in-practice-an-example-with-keras-and-tensorflow-2-0-52a96746123e) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/003-model-regularization/model-regularization.ipynb)
* [Batch Normalization in practice](https://medium.com/@bindiatwork/batch-normalization-in-practice-an-example-with-keras-and-tensorflow-2-0-b1ec28bde96f) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/004-batch-norm/batch-normalization.ipynb)
* [Early Stopping in practice](https://medium.com/@bindiatwork/a-practical-introduction-to-early-stopping-in-machine-learning-550ac88bc8fd) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/005-early-stopping/early-stopping.ipynb)
* [Learning Rate schedules in Practice](https://medium.com/@bindiatwork/learning-rate-schedule-in-practice-an-example-with-keras-and-tensorflow-2-0-2f48b2888a0c) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/006-learning-rate-schedules/learning-rate-schedules.ipynb)
* [Keras Callbacks in Practice](https://medium.com/@bindiatwork/a-practical-introduction-to-keras-callbacks-in-tensorflow-2-705d0c584966) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/007-keras-callback/keras-callbacks.ipynb)
* [Keras Custom Callbacks](https://bindichen.medium.com/building-custom-callbacks-with-keras-and-tensorflow-2-85e1b79915a3) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/008-keras-custom-callback/keras-custom-callback.ipynb)
* [7 popular activation functions in Deep Learning](https://bindichen.medium.com/7-popular-activation-functions-you-should-know-in-deep-learning-and-how-to-use-them-with-keras-and-27b4d838dfe6) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/010-popular-activation-functions/popular-activation-functions.ipynb)
* [Why ReLU in Deep Learning and the best practice](https://towardsdatascience.com/why-rectified-linear-unit-relu-in-deep-learning-and-the-best-practice-to-use-it-with-tensorflow-e9880933b7ef) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](tensorflow2/011-relu/relu-and-best-practice.ipynb)

### PyTorch

TBA

## Scikit-Learn and General Machine Learning

* [A Practical Introduction to Grid Search, Random Search, and Bayes Search](https://bindichen.medium.com/a-practical-introduction-to-grid-search-random-search-and-bayes-search-d5580b1d941d) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](traditional-machine-learning/005-grid-search-vs-random-search-vs-bayes-search/gridsearch-vs-randomsearch-vs-bayessearch.ipynb)
* [A Practical Introduction to 9 Regression Algorithms](https://bindichen.medium.com/a-practical-introduction-to-9-regression-algorithms-389057f86eb9) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](traditional-machine-learning/001-regression-algorithms/regression-algorithms.ipynb)
* Train-Test split and Cross-Validation you should know in Machine Learning (TBA) | [![View on Github](https://img.shields.io/badge/Github-Notebook-orange?logo=Github)](traditional-machine-learning/006-train-test-split-and-cross-validation/train-test-and-cross-validation.ipynb)

