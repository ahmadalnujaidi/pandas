import pandas as pd # pyright: ignore[reportMissingModuleSource]
print("Pandas version:", pd.__version__)

df = pd.read_csv('./data/data.csv')
#print(df)

# print all
#print(df.to_string())


## read json
df = pd.read_json('./data/data.json')
print(df.head())