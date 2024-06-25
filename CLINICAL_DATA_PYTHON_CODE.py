#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd Desktop


# In[2]:


cd HOSPITAL_CLINICAL_ML_CODE


# ### Set up the Notebook

# In[3]:


# Import Necessary Libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))



# #### Merge the two csv from the 'Clinical-dataset'

# In[4]:


import pandas as pd

# Load the CSV files
csv_file1 = 'Clinical Data_Discovery_Cohort.csv'
csv_file2 = 'Clinical_Data_Validation_Cohort.xlsx'

df1 = pd.read_csv(csv_file1)
df2 = pd.read_excel(csv_file2)

# Merge the two dataframes into a new one named 'data'
data = pd.concat([df1, df2], ignore_index=True)

# Now 'data' contains the merged data from both CSV and Excel files


# In[6]:


# Check for the first 10 rows
print("First 20 rows")
data.head(20)


# In[7]:


# Take a look at the last rows
print("Last rows")
data.tail(10)


# - Descriptive Statistics for numerical Values

# In[8]:


data.describe(exclude='O')


# In[9]:


# Calculate the percentage of NaN values for each column
nan_percentage = (data.isna().mean() * 100).round(2)

# Display the result
print(nan_percentage)


# In[10]:


# Calculate the total percentage of NaN values in the entire DataFrame
total_nan_percentage = (data.isna().mean().mean() * 100).round(2)

# Display the result
print("Total Percentage of NaN Values in the DataFrame:", total_nan_percentage, "%")


# - Note: It seems like this DataFrame has a lot of Missing values!

# #### Data Cleaning

# In[11]:


# Check for Missing values with the .isnull().sum
data.isnull().sum()


# In[12]:


# Calculate the total amount of Missing values
data.isnull().sum().sum()


# In[13]:


# Replace all NaN values in the entire DataFrame with 0
data.fillna(0, inplace=True)


# In[14]:


# Corroborate if the formula above worked
data.isnull().sum().sum()


# In[15]:


# Check the data types
data.dtypes


# In[16]:


# Get the info of the data
data.info()


# #### Analysis of the Information!

# - What is the average age of the patients of the dataset?

# In[17]:


average_age = data['Age'].mean()
print(average_age)


# - How many patients in the dataset are alive and how many are dead?

# In[18]:


alive_count = data[data['Dead or Alive'] == 'Alive']['PatientID'].count()
print(alive_count)


# In[19]:


dead_count = data[data['Dead or Alive'] == 'Dead']['PatientID'].count()
print(dead_count)


# - What is the distribution of tumor sizes (cm) in the dataset?
# 

# In[20]:


tumor_size_distribution = data['Tumor size (cm)'].value_counts()
print(tumor_size_distribution)


# - How many patients have a Grade of 1, 2, and 3, respectively?
# 

# In[21]:


grade_counts = data['Grade'].value_counts()
print(grade_counts)


# - What is the average survival time (in days) of the patients in the dataset?
# 

# In[22]:


average_survival_time = data['Survival time (days)'].mean()
print(average_survival_time)


# - How many patients are smokers(cigarette column is 'Yes') and how many are non smokers(cigarette column is 'No')?

# In[23]:


smoker_count = data[data['Cigarette'] == 'Yes']['PatientID'].count()
print(smoker_count)


# In[24]:


non_smoker_count = data[data['Cigarette'] == 'No']['PatientID'].count()
print(non_smoker_count)


# - What is the distribution of 'Type.Adjuvant' among the patients?
# 

# In[25]:


type_adjuvant_distribution = data['Type.Adjuvant'].value_counts()
print(type_adjuvant_distribution)


# - Is there any correlation between 'Age' and 'Survival time (days)' for patients in the dataset?
# 

# In[26]:


correlation = data[['Age', 'Survival time (days)']].corr()
print(correlation)


# #### Data Visualization

# - Tumor size distribution

# In[27]:


tumor_size_distribution = data['Tumor size (cm)'].value_counts().reset_index()
tumor_size_distribution.columns = ['Tumor Size (cm)', 'Count']

# Create a custom color scale based on tumor size values
color_scale = px.colors.sequential.RdBu[::-1]

# Create a bar plot with a different color for each tumor size
fig = px.bar(
    tumor_size_distribution,
    x='Tumor Size (cm)',
    y='Count',
    labels={'x': 'Tumor Size (cm)', 'y': 'Count'},
    title='Tumor Size Distribution',
    color='Tumor Size (cm)',
    color_continuous_scale=color_scale
)

# Show the interactive plot
fig.show()


# - Average survival time

# In[28]:


# Calculate the average survival time
average_survival_time = data['Survival time (days)'].mean()

# Create a DataFrame for plotting
average_survival_df = pd.DataFrame({'Metric': ['Average Survival Time'],
                                    'Value': [average_survival_time]})

# Create a custom color scale
color_scale = px.colors.sequential.Plasma

# Create a bar plot with a different color for the average survival time
fig = px.bar(
    average_survival_df,
    x='Metric',
    y='Value',
    text='Value',
    color='Value',
    color_continuous_scale=color_scale,
    labels={'Value': 'Average Survival Time (days)'},
    title='Average Survival Time'
)

# Show the interactive plot
fig.show()


# - Correlation between Age and Survival Time

# In[29]:


correlation = data[['Age', 'Survival time (days)']].corr()

# Create a scatter plot with different colors based on 'Event (death: 1, alive: 0)'
fig = px.scatter(
    data,
    x='Age',
    y='Survival time (days)',
    color='Event (death: 1, alive: 0)',
    title='Scatter Plot: Age vs. Survival Time',
    labels={'Age': 'Age', 'Survival time (days)': 'Survival Time (days)'},
    color_discrete_map={0: 'blue', 1: 'red'}  # Define colors for 0 and 1
)

# Show the interactive plot
fig.show()


# - Distribution of Grades with Different Colors

# In[30]:


grade_counts = data['Grade'].value_counts().reset_index()
grade_counts.columns = ['Grade', 'Count']

# Create a custom color scale with unique colors for each grade
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Add more colors if needed

# Create a bar plot with different colors
fig = px.bar(
    grade_counts,
    x='Grade',
    y='Count',
    title='Distribution of Grades',
    labels={'Grade': 'Grade', 'Count': 'Count'},
    color='Grade',
    color_discrete_sequence=colors
)

# Show the interactive plot
fig.show()


# -  How many patients in the dataset are alive and how many are dead?

# In[31]:


alive_count = data[data['Dead or Alive'] == 'Alive']['PatientID'].count()
dead_count = data[data['Dead or Alive'] == 'Dead']['PatientID'].count()

# Create a DataFrame for the pie chart
status_counts = pd.DataFrame({'Status': ['Alive', 'Dead'],
                              'Count': [alive_count, dead_count]})

# Define colors for the pie chart
colors = ['#1f77b4', '#d62728']

# Create an interactive pie chart with different colors
fig = px.pie(
    status_counts,
    names='Status',
    values='Count',
    title='Distribution of Patients by Status',
    color_discrete_sequence=colors
)

# Show the interactive plot
fig.show()


# In[32]:


data.columns


# - Distribution of Dead by Gender

# In[33]:


# Filter the DataFrame for only 'Dead' patients
dead_patients = data[data['Dead or Alive'] == 'Dead']

# Calculate the count of 'M' and 'F' patients among the dead
gender_counts = dead_patients['sex'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Define colors for the bar plot
colors = ['#1f77b4', '#ff7f0e']

# Create an interactive bar plot with different colors
fig = px.bar(
    gender_counts,
    x='Gender',
    y='Count',
    title='Distribution of Dead Patients by Gender',
    labels={'Gender': 'Gender', 'Count': 'Count'},
    color='Gender',
    color_discrete_sequence=colors
)

# Show the interactive plot
fig.show()


# In[ ]:




