
# coding: utf-8

# # Lesson 4
# by Cheyenne Krampitz

# ###### 1) Create 3 variables for name (first and last), age and hometown. Assign to these variables your own name, age and hometown. Now, recreate the following sentence using variable assignment and the ‘print’ command in Python: 
# “I am &lt;Your name here&gt;. I am &lt;age&gt; years old. I’m from &lt;hometown&gt;”
# a) Now, use a string method to make your name lower case. Print the all lower case
# version of your name.
# b) Now use a string method to make your full name a proper noun. Print this version of
# your name.

# In[23]:


Name = "Cheyenne Krampitz"
Age = "20"
Hometown = "Owatonna"
print("I am " + Name + ". I am " + Age + " years old. I'm from " + Hometown)


# In[12]:


print(str.lower(Name))


# In[13]:


print(str.title(Name))


# ###### 2) Using the ‘replace’ method, replace all “I am” with “he is” or “she is” and all “I’m” with “he’s” or “she’s”.

# In[14]:


str = "I am Cheyenne Krampitz. I am 20 years old. I'm from Owatonna"
print(str.replace("I am", "he is").replace("I'm", "she's"))


# ###### 3) Return a boolean response indicating whether the length of your original sentence (in #1) is greater than your age plus 40.

# In[24]:


str = "I am Cheyenne Krampitz. I am 20 years old. I'm from Owatonna"
bool(len(str)>(20+40))

