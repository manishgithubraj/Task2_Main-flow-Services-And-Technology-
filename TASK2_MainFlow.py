#!/usr/bin/env python
# coding: utf-8

# # Load a CSV file into a PandasDataFrame. Perform operations likefiltering data based on conditions, handlingmissing values, and calculating summarystatistics.

# In[3]:


get_ipython().system('pip install matplotlib')


# In[4]:


get_ipython().system('pip install scipy')


# In[5]:


import pandas as pd


# In[11]:


data = pd.read_csv("E:\\Task 2 Main Flow\\01.Data Cleaning and Preprocessing.csv")


# In[12]:


type(data)


# In[13]:


data.info


# In[14]:


data.describe() #descriptive statistics


# In[15]:


data = data.drop_duplicates()
data


# In[16]:


data.isnull()


# In[17]:


data.isnull().sum()


# In[18]:


data.notnull()


# In[19]:


data.isnull().sum().sum()


# In[20]:


data2 = data.fillna(value=0)
data2


# In[21]:


data2.isnull().sum().sum()


# In[22]:


data


# In[23]:


data3 = data.fillna(method='pad')
data3


# In[24]:


#filling null values with the next value
data4=data.fillna(method='bfill')
data4


# In[25]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# In[26]:


#detect the outlier using IQR
data2.columns


# In[27]:


data2.drop(['Observation'], axis=1, inplace=True)
data2.columns


# In[28]:


Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR= Q3 - Q1
print(IQR)


# In[29]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[30]:


data2.describe()


# 
