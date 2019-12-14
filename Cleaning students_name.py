#%%
import pandas as pd
import os
#%%
# Load Files
#school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")
#%%
# Read the school data file and store it in a Pandas DataFrame.
#school_data_df = pd.read_csv(school_data_to_load)
#school_data_df

# %%
#school_data_df.head()
#school_data_df.tail()
#school_data_df.describe()

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
student_names = student_data_df["student_name"].tolist()
student_names

# %%
# Create a new list and use it for the for loop to iterate through the list.
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)
#%%
# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)# %%


# %%
# Add the suffixes less than or equal to 3 to a new list.
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])

print(suffixes)

# %%
# Get the unique items in the "prefixes" list.
set(prefixes) 
#%%
# Get the unique items in the "suffixes" list.
set(suffixes) 

# %%
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
#%%
# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# %%
# Put the cleaned students' names in another list.
student_names_cleaned = student_data_df["student_name"].tolist()
student_names_cleaned
#%%
# Create a new list and use it for the for loop to iterate through the list.
students_fixed_cleaned = []

# Use an if statement to check the length of the name.

# If the name is greater than or equal to 3, add the name to the list.

for name in student_names_cleaned:
    if len(name.split()) >= 3:
        students_fixed_cleaned.append(name)

# Get the length of the students' names that are greater than or equal to 3.
len(students_fixed_cleaned)

# %%
