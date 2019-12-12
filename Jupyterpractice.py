
# %%
# List of high schools
high_schools = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]
#%%
import pandas as pd
#school_series = pd.Series(high_schools)
#school_series
# %%
print(school_series.values)

# %%
# A dictionary of high schools
high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]
#%%
school_df = pd.DataFrame(high_school_dicts)
school_df

# %%
# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]

type_of_school = ["District", "District", "Charter", "District","Charter"]
#%%
school_df2 = pd.DataFrame()
high_school_dicts2 = {'School ID': school_id, 'School Name':school_name, 'Type': type_of_school}

# %%
school_df2 = pd.DataFrame(high_school_dicts2)
school_df2
# %%
school_df2.columns

# %%
schools_id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
high_schools_name = ["Huang High School",  "Figueroa High School", "Shelton High School", "Hernandez High School","Griffin High School","Wilson High School", "Cabrera High School", "Bailey High School", "Holden High School", "Pena High School", "Wright High School","Rodriguez High School", "Johnson High School", "Ford High School", "Thomas High School"]
school_type = ['District', 'District', 'Cherter', 'District', 'Charter', 'Charter','Charter','District','Charter','Charter','Charter','District','District','District','Charter']
#%%
school_df3 = pd.DataFrame()
school_df3['School Id'] = schools_id
school_df3['high schools name'] = high_schools_name
school_df3['school type'] = school_type
school_df3
# %%
