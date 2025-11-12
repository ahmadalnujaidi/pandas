import pandas as pd
print(pd.__version__)

"""
# series = a pandas 1-dimensional labeled array capable of holding any data type

data = [100, 101, 102, 103, 107, 200, 207]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# print(series)

# Accessing elements
print(series['b'])  # Access by label
series["c"] = 150  # Modifying value by label
print(series.loc['c'])  # Access by label using loc
print(series.iloc[0])  # Access by position using iloc - integer location


# Series filter
print(series[series >= 150])  # Filter series for values greater than 150
"""

cal = {
    'Day 1': 1750,
    'Day 2': 2100,
    'Day 3': 1700,
}

series = pd.Series(cal)
print(series)

series["Day 3"] += 500
print(series)
print(series[series >= 2000])  # Filter series for values greater than or equal to 2000