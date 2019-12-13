#%%
import pandas as pd
import os
#%%
# Load Files
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")
#%%
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df

# %%
#school_data_df.head()
#school_data_df.tail()
school_data_df.describe()

#%%
# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df

# %%
# Determine if there are any missing values in the school data.
#school_data_df.count()
student_data_df.count()

# %%
student_data_df.isnull().sum()
#%%
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
#%%
# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
#%%
student_data_df.head(10)
#%%
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()

# %%
student_count = school_data_complete_df["Student ID"].count()

# %%
# Calculate the total number of schools
school_count = len(school_data_complete_df["school_name"].unique())
school_count
# %%
groupby_school_df = school_data_complete_df.groupby('school_name')
groupby_school_totalbudget = groupby_school_df['budget'].sum()   

# %%
groupby_school_totalbudget['budget'].sum() 
