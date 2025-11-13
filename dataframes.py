import pandas as pd
#print("Pandas version:", pd.__version__)

# Dataframe = a tabular DS with rows and columns

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
}

df = pd.DataFrame(data) #index = ["emp1", "emp2", "emp3", "emp4"]
print(df)
print(df.loc[0]) #loc = location loc = by label
print(df.iloc[1]) #iloc = integer location iloc = by position

# add new column
df["Salary"] = [50000, 60000, 55000, 70000]
print(df)

# add new row
new_employee = pd.DataFrame({
    "Name": ["Eve", "ahmad"],
    "Age": [28, 29],
    "Salary": [65000, 62000]
}, index=[100, 101])
df = pd.concat([df, new_employee], ignore_index=False)
print(df)