#%%
import pandas as pd
#%%
csvFile: str = "/Users/hebamaly/School_District_Analysis/Live Session4/Pokemon_input.csv"

#read this csv into a pandas dataframe
Pokemondf = pd.read_csv(csvFile)
print(Pokemondf.count())
#%%
groupByType = Pokemondf.groupby(['Type 1'])
print(groupByType)
#%%
groupByTypeAvg = groupByType['Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary'].mean()

# %%
