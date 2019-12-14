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
#%%
# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget
#%%
# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score
#%%
# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score
#%%
# (filter)Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()
#%%
# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
#%%
# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()

# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
print(passing_math_count)
print(passing_reading_count)
#%%
# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100

# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100

print(passing_reading_percentage)
print(passing_math_percentage)
#%%
# Calculate the overall passing percentage.
overall_passing_percentage = (passing_math_percentage + passing_reading_percentage ) / 2
#%%
# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df
#%%
# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]
#%%
# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]
#%%
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)
#%%
district_summary_df
#%%
# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df
#%%
# Determine the school type.
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_types
#%%
df = pd.DataFrame(per_school_types)
df
#%%
# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts
#%%
# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts
#%%
# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget
#%%
groupbyschool_budget = school_data_complete_df.groupby('school_name')
groupbyschool_totbudget = groupbyschool_budget['budget'].value_counts()
groupbyschool_totbudget
#%%
# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita
#%%
# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages
#%%
# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
#%%
per_school_math

#%%
groupbyschool_math_score = school_data_complete_df.groupby('school_name')
groupbyschool_Avg_math = groupbyschool_math_score[(groupbyschool_math_score['math_score']>=70)].mean()
groupbyschool_Avg_math
#%%
# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
#%%
# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
#%%
# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
#%%
 #Calculate the overall passing percentage.
per_overall_passing_percentage = (per_school_passing_math + per_school_passing_reading ) / 2
#%%
# Adding a list of values with keys to create a new DataFrame.

per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()
#%%
# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# Display the data frame
per_school_summary_df.head()
#%%
# Reorder the columns in the order you want them to appear.
new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
per_school_summary_df = per_school_summary_df[new_column_order]

per_school_summary_df.head()
#%%
# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()
#%%
# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()
# %%
groupby_school_df = school_data_complete_df.groupby('school_name')
groupby_school_totalbudget = groupby_school_df['budget'].sum()   


# %%
