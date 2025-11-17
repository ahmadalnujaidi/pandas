import pandas as pd
#print(pd.__version__)

# aggregate functions = reduces a set of values into a single summary value - used to summarize and analyze data - often used with the groupby() function

df = pd.read_csv('./data/data.csv')

# whole data frame
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())

# single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

group = df.groupby("Type1") # returns a series object - they all get grouped by type1 and we query those groups to find each groups mean, sum etc...
# an object
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())