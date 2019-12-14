#%%
import pandas as pd
import os
#%%
cleaning_data_file = os.path.join('Resources', 'missing_grades.csv')
#%%
missing_grades_df = pd.read_csv(cleaning_data_file)
missing_grades_df

# %%
missing_grades_df.isnull().sum()

# %%
missing_grades_df.fillna(85.0)

# %%
missing_grades_df.dtypes

# %%
