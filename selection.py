import pandas as pd # type: ignore
#print("Pandas version:", pd.__version__)

df = pd.read_csv('./data/data.csv', index_col="Name") # set Name as index

# selection by column
#print(df["Name"]) #.to_string() if u want all
#print(df["Height"])

#print(df[["Name","Height","Weight"]].to_string())


# selection by row - must set index_col in read_csv
#print(df.loc["Pikachu", ["Height", "Weight"]])
print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]])
print(df.iloc[0:11:2, 0:3]) # step 2 - 3 columns

pokemon = input("Enter pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")