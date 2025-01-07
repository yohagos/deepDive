# Pandas
#
# Pandas is an open source, high-performance, easy-to-use data
# structures and data analysis tools for the Python programming language.
# Pandas adds data structures and tools designed to work with table-like
# data which is Series and Data Frames. Pandas provides tools for data manipulation:
#
#     reshaping
#     merging
#     sorting
#     slicing
#     aggregation
#     imputation. If you are using anaconda, you do not have install pandas.


# Pandas data structure is based on Series and DataFrames.
#
# A series is a column and a DataFrame is a multidimensional table
# made up of collection of series. In order to create a pandas series
# we should use numpy to create a one dimensional arrays or a python list.
# Let us see an example of a series:
#
# Names Pandas Series

import pandas as pd
import numpy as np

# nums = [1,2,3,4,5]
# s = pd.Series(nums)
# print(s)

# nums = [1, 2, 3, 4, 5]
# s = pd.Series(nums, index=[1, 2, 3, 4, 5])
# print(s)
#
# fruits = ['Orange','Banana','Mango']
# fruits = pd.Series(fruits, index=[1, 2, 3])
# print(fruits)
#
#
# dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
# s = pd.Series(dct)
# print(s)
#
# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)



# data = [
#     ['Asabeneh', 'Finland', 'Helsink'],
#     ['David', 'UK', 'London'],
#     ['John', 'Sweden', 'Stockholm']
# ]
# df = pd.DataFrame(data, columns=['Names','Country','City'])
# print(df)
#
# print()
#
# data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
#     'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
# df = pd.DataFrame(data)
# print(df)
#
# print()
#
# data = [
#     {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
#     {'Name': 'David', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
# df = pd.DataFrame(data)
# print(df)
#
# df = pd.read_csv('example_data.csv')
# print(df)
# print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
# print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
# print(df.shape) # as you can see 10000 rows and three columns
# print(df.columns)
#
# heights = df['Height'] # this is now a series
# print(heights)
# weights = df['Weight'] # this is now a series
# print(weights)
#
# print(heights.describe()) # give statisical information about height data
# print(weights.describe())
# print(df.describe())  # describe can also give statistical information from a dataFrame



# Modifying a DataFrame
# Modifying a DataFrame: * We can create a new DataFrame * We can create a new column
# and add it to the DataFrame, * we can remove an existing column from a DataFrame,
# * we can modify an existing column in a DataFrame, * we can change the data type of
# column values in the DataFrame


data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
weights = [74, 78, 69]
df['Weight'] = weights
print(df)
heights = [173, 175, 169]
df['Height'] = heights
print(df)
df['Height'] = df['Height'] * 0.01
print(df)


# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

df['BMI'] = bmi
print(df)

birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)


ages = df['Current Year'] - df['Birth Year']
print(ages)

df['Ages'] = ages
print(df)

print(df[df['Ages'] > 120])