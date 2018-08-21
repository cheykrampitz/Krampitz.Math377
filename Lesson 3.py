
# coding: utf-8

# # Lesson 3
# by Cheyenne Krampitz

# ###### 1) At the beginning of your Jupyter notebook, include the following code chunk. This will load required packages:

# In[2]:


import numpy as np 
from datascience import * 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots 
plots.style.use('fivethirtyeight')
import warnings 
warnings.simplefilter(action="ignore", category=FutureWarning)


# ###### 2) Use basic Python operators to find the number of seconds in the month of June. Find the number of seconds that have lapsed between 1 June at noon and 14 Aug, 9:30 AM.

# In[6]:


Hours = 30 * 24
Minutes = Hours * 60 
Seconds = Minutes * 60
print(Seconds)


# In[7]:


Days = 74
Hours = Days * 24
Minutes = Hours * 60 
Seconds = Minutes * 60 
Addhours = 21.5 
Addmin = Addhours * 60 
Addsec = Addmin * 60 
Finalsec = Seconds + Addsec
print(Finalsec)


# ###### 3) Import a table (‘world_population.csv’) and find:
#    a. The population in 2015 (the dataset begins at 1950).
#    
#    b. The population growth between 1950 and 2015.
#    
#    c. The average annual growth rate over the course of the dataset.

# In[16]:


population = Table.read_table('Downloads\world_population.csv')


# In[18]:


print("The worlds population in 2015 was" int(population.where("year",2015).column("Population"))


# In[ ]:


intial = 

(final/inital) ** (1/year) - 1

