#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


pd.__version__


# In[5]:


list_s=[1,2,-3,6.2,'data values']
print(list_s)


# In[6]:


series1=pd.Series(list_s)
print(series1)


# In[7]:


type(series1)


# In[8]:


series2=pd.Series([1,2,3,4])
print(series2)


# In[9]:


empty_s=pd.Series([])
print(empty_s)


# In[10]:


series3=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(series3)


# In[11]:


series3=pd.Series([1,2,3,4],index=['a','b','c','d'],dtype=float)
print(series3)


# In[12]:


series3=pd.Series([1,2,3,4],index=['a','b','c','d'],dtype=float,name='data values')
print(series3)


# In[13]:


scalar_s=pd.Series(0.5)
print(scalar_s)


# In[14]:


scalar_s=pd.Series(0.5,index=[1,2,3])
print(scalar_s)


# In[ ]:





# In[17]:


scalar_s[2]


# In[ ]:





# In[15]:


dict_s=pd.Series({'a':1,'b':2})
print(dict_s)


# In[2]:


import pandas as pd


# In[3]:


emt_df = pd.DataFrame()
print(emt_df)


# 

# In[4]:


lst=['a','b','c']
print(lst)


# In[5]:


df1=pd.DataFrame(lst)
print(df1)


# In[6]:


df1


# In[7]:


ls_of_ls = [[1,2,3],[2,3,4],[4,5,6]]
print(ls_of_ls)


# In[8]:


df2=pd.DataFrame(ls_of_ls)
df2


# In[9]:


dict1={'ID':[11,22,33,44]}
dict1


# In[11]:


df3=pd.DataFrame(dict1)
df3


# In[12]:


dict1={'ID':[11,22,33,44],'SN':[1,2,3,4]}
dict1


# In[13]:


df3=pd.DataFrame(dict1)
df3


# In[18]:


ls_dict=[{'a':1,'b':2},{'a':3,'b':4,'c':5}]
df5=pd.DataFrame(ls_dict)
df5


# In[23]:


import pandas as pd


# In[25]:


help(pd.read_csv)


# In[30]:


pd.read_csv('C:\\Users\RAJIV\\Desktop\\NIELIT_PATNA\\50_Startups.csv')


# In[31]:


pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\Energy Data.csv')


# In[32]:


import os


# In[33]:


print(os.getcwd())


# In[34]:


import pandas as pd


# In[41]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip')
df


# In[42]:


type(df)


# In[43]:


df.columns


# In[46]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',nrows=5)
df


# In[47]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',usecols=[0])
df


# In[48]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',usecols=[0,1])
df


# In[51]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',usecols=[2,4,5])
df


# In[58]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip')
df


# In[59]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',index_col='country')
df


# In[62]:


df=pd.read_csv('C:\\Users\\RAJIV\\Desktop\\NIELIT_PATNA\\drinks.zip',skiprows=6)
df


# In[ ]:




