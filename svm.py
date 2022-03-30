#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


dataset=pd.read_csv("student_scores.csv")


# In[4]:


print(dataset)


# In[5]:


dataset.head()


# In[16]:


dataset.tail()


# In[17]:



dataset.describe()


# In[20]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x_test,y_test,testscore=0.2)


# In[21]:


from sklearn import support vector machine
classifier=classifier.support vector machine()
classifier.fit(y_train,y_predict)
classifier.predict(x_test)


# In[22]:


x=dataset.iloc[:1]


# In[ ]:




