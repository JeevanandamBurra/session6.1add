
# coding: utf-8

# ## 1. Read the dataset using pandas.

# In[3]:


import pandas as pd
import numpy as np


# In[10]:


Movies=pd.read_csv("E:/Add/Add_ex/movies.csv")
Rating1=pd.read_csv("E:/Add/Add_ex/ratings.csv")
Tags=pd.read_csv("E:/Add/Add_ex/tags.csv")
Rating=Rating1.head(1500)
mv=Movies.head(1500)


# ## 2. Extract the first row from tags and print its type.

# In[13]:


#Tags.iloc[0]
type(Tags.iloc[0])


# ## 3. Extract row 0, 11, 2000 from tags DataFrame.

# In[16]:


Tags.iloc[[0,11,2000]]


# ## 4. Print index, columns of the DataFrame.

# In[21]:


Tags.index


# In[28]:


Tags.columns


# ## 5. Calculate descriptive statistics for the 'ratings' column of the ratings DataFrame. Verify using describe().

# In[31]:


Rating.head()


# In[46]:


R_sum=Rating['rating'].sum()
print(R_sum)
R_Mean=Rating['rating'].mean()
print(R_Mean)
min1=Rating['rating'].min()
print(min1)
max1=Rating['rating'].max()
print(max1)
Count1=Rating['rating'].count()
print(Count1)
sd=Rating['rating'].std()
print(sd)
qun1=Rating['rating'].quantile(0.25)
print(qun1)
qun2=Rating['rating'].quantile(0.5)
print(qun2)
qun3=Rating['rating'].quantile(0.75)
print(qun3)


# In[34]:


Rating['rating'].describe()


# ## 6. Filter out ratings with rating > 4
# 

# In[7]:


Rating[Rating.rating > 4].head()


# ## 7. Find how many null values, missing values are present. Deal with them. Print out how many rows have been modified.

# In[40]:


R_Mis=Tags[Tags.isnull().any(axis=1)]
len(R_Mis)


# In[49]:


Tags.isnull().sum()


# In[42]:


mv.isnull().sum()


# In[43]:


Rating.isnull().sum()


# In[7]:


Tags.dropna(inplace=True)


# In[8]:


Tags.isnull().sum()


# ## 8. Filter out movies from the movies DataFrame that are of type 'Animation'.

# In[11]:


mv.head()


# In[13]:


mv[mv['genres'].str.contains('Animation')]


# ## 9. Find the average rating of movies.

# In[15]:


Rating.head()


# In[19]:


avg_mv = Rating.groupby('movieId')
print(avg_mv.mean().head())


# ## 10. Perform an inner join of movies and tags based on movieId.

# In[21]:


mv_tg=pd.merge(mv, Tags, how='inner',on=['movieId'])
mv_tg.head()


# ## 11. Print out the 5 movies that belong to the Comedy genre and have rating greater than 4.

# In[24]:


mv_rating=pd.merge(mv,Rating,how='inner',on=['movieId']).head(1000)
mv_rating.head()


# In[35]:


mv_rating[(mv_rating.genres.str.contains('Comedy')) & (mv_rating.rating>4)].head()


# ## 12. Split 'genres' into multiple columns.

# In[48]:


mv.head()


# In[51]:


mv['genres'].str.split('|',expand=True).head()


# ## 13. Extract year from title e.g. (1995).

# In[52]:


mv.head(3)


# In[78]:


mv.title.str.extract('(\d+)',expand=True).head()


# ## 14. Select rows based on timestamps later than 2015-02-01.

# In[73]:


from datetime import datetime
Tags.timestamp = pd.to_datetime(Tags['timestamp'],unit='s')

Tags.head()


# In[75]:


Tags[Tags.timestamp> pd.to_datetime('2015-02-01')].head()


# ## 15. Sort the tags DataFrame based on timestamp.

# In[76]:


Tags.head()


# In[77]:


Tags.sort_values(by='timestamp',ascending=True).head()

