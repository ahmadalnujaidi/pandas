import pandas as pd
#print("Pandas version:", pd.__version__)

# filtering = keeping the rows that match a condition

df = pd.read_csv('./data/data.csv')
print(df)

#tall_pokemon = df[df["Height"] >= 2]
#print(tall_pokemon)

heavy_pokemon = df[df["Weight"] > 100]
print(heavy_pokemon)

legendary_pokemon = df[df["Legendary"] == 1]
print(legendary_pokemon)

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)

hw_pokemon = df[(df["Type1"] == "Grass") & (df["Weight"] < 20) & (df["Type2"] == "Psychic")]
print(hw_pokemon)