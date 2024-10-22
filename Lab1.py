#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


survey_data = pd.read_csv("/Users/emilyhenderson/Library/CloudStorage/OneDrive-TexasTechUniversity/cleaned_surveydata.csv")


# In[ ]:


#3b1
gender_group = survey_data[["meal_out", "food_rating", "interest"]].groupby(survey_data['gender'])
gender_group.mean()


# In[ ]:


#3b2
factor_group = survey_data[["meal_out", "food_rating", "interest"]].groupby(survey_data['factor'])
factor_group.mean()


# In[ ]:


#c1
plt.hist(survey_data['meal_out'], bins = 5, color = 'green', edgecolor = 'black')
plt.xlabel('Number of Times Eating Out per Week')
plt.ylabel('Frequency')
sns.set_style("whitegrid")
plt.title('Histogram - Frequency of Getting Food from Restaurants')
plt.show()


# In[ ]:


#c1
plt.hist(survey_data['food_rating'], bins = 10, color = 'blue', edgecolor = 'black')
plt.xlabel('Overall Rating')
plt.ylabel('Frequency')
sns.set_style("whitegrid")
plt.title('Histogram - Overall Rating of Nearby Restaurants')
plt.show()


# In[ ]:


#c1
plt.hist(survey_data['interest'], bins = 5, color = 'red', edgecolor = 'black')
plt.xlabel('Interest Score')
plt.ylabel('Frequency')
sns.set_style("whitegrid")
plt.title('Histogram - Scores of Interest in the New Diner')
plt.show()


# In[ ]:


#c2
plt.boxplot(survey_data['meal_out'])
plt.title('Boxplot - Frequency of Getting Food from Restaurants')
plt.show()


# In[ ]:


#c2
plt.boxplot(survey_data['food_rating'])
plt.title('Boxplot - Overall Rating of Nearby Restaurants')
plt.show()


# In[ ]:


#c2
plt.boxplot(survey_data['interest'])
plt.title('Boxplot - Score of Interest in New Diner')
plt.show()


# In[ ]:


#c3
sns.scatterplot(x = 'meal_out', y = 'interest', data = survey_data, color = 'blue')


# In[ ]:


#c4
sns.scatterplot(x = 'meal_out', y = 'interest', hue = 'food_rating', data = survey_data, palette = 'magma')
plt.xlabel('Frequency of Getting Food from Restaurants')
plt.ylabel('Score of Interest in New Diner')
plt.title('Relationship between Eating Out and Interest in New Diner Grouped By Local Rating')
plt.show()


# In[ ]:




