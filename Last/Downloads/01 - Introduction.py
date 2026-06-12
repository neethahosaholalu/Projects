#!/usr/bin/env python
# coding: utf-8

# # Practical 1 - Introduction
# 
# This notebook introduces you to the essential tools we will be using in this module. Most of you will be familiar with those from last semester's "Foundations of Data Science" module. Consider this as a refresher. 
# 
# You work through this notebook at your own pace. Make sure you understand and solve all tasks. Bring any questions, comments, suggestions to next week's practical session.

# ## 1 - Jupyter notebooks
# 
# Jupyter notebooks can contain code, text, and images. You can edit the text and change the code. The first part of this notebook recaps the basics of notebooks and the possibilities they offer to structure text. This is useful e.g. for generating reports. 
# 
# ### 1.1 Run and edit some code
# Below is a code cell. You recognise it by the `In [ ]:` next to it. 
# 
# **Task:** Run the code by selecting the cell with the mouse or with the arrow keys, and press Shift+Enter.
# 
# **Task:** Make it print "Data Science rocks!"

# In[1]:


print("Hello world")


# In case your code contains an error, jupyter will show you the Error or Exception it created that helps you locate the error. 
# 
# **Task:** Fix the code below so that it doesn't create an error. Use the information provied by the Error traceback. (Yes, this will change the semantics of the last line, no worries we are not interested in the result.)

# In[2]:


a = 1 
b = 2
c = 8
d = (a+b)/(b-c) 


# ### 1.3 edit some text
# Below is a text(markdown) cell. There are four types of cells. You can change the type of a cell by selecting the type in the top line. It supports formatting using Markdown. Select it and observe how the raw text appears, and what is used for formatting. 
# 
# **Task:** Change the cell below from a code to a markdown cell.

# This is code, but it wants to be text!

# I'm a text cell. I support headings of different levels:
# # heading 1
# ## heading 2
# ### heading 3
# #### heading 4
# 
# **Task**: is there a level 4 heading? Find out yourself!

# Please write your attempt for a level 4 heading below in this cell

# #### heading 4

# In this cell, observe how *slanted* and **bold** font is created. 
# 
# **Task:** Make the sentence "I'm slanted." appear in *slanted* (italic) font, and the sentence "I'm bold!" appear in **bold** font.

# *I'm slanted.*
# 
# **I'm bold!**

# ### 1.4 Getting help
# 
# Jupyter notebooks support two ways of help: 
# 1. help for Jupyter notebooks via the "Help menu".
# 2. in-line help for Python commands and objects via the `?` command.
# 
# **Task:** Explore the Help menu. Take the User interface tour.
# 
# **Task:** Execute the below cell to obtain the python documentation for the `print` function. Exit the help viewer by pressing `q`.
# 
# **Task:** Modify the cell to look up the python documentation for the `help` function.

# In[3]:


get_ipython().run_line_magic('pinfo', 'print')


# In[4]:


get_ipython().run_line_magic('pinfo', 'print')


# ### 1.5 Saving and loading Jupyter notebooks
# 
# Save this notebook either by pressing the icon in the top left, or by hitting Ctrl+S.
# 
# Notebooks are plain-text files in a format called JSON. 
# 
# **Task:** Use the file manager to navigate to the location of this notebook. Open the notebook with a text editor and verify that it's plain text. 

# **Result --> I got my file in plain text format when I opened in notebook**

# ## 2 - The NumPy module
# 
# Modules are imported using the `import` statement. To save us some typing, we usually use the `import ... as ...` idiom that lets us assing a shorthand for external modules. 
# 
# **Task:** Run the cell below to import `numpy`, under the name `np`.

# In[5]:


import numpy as np


# ### 2.1 Arrays
# 
# The essential functionality of the `numpy` module is to provide an `array` class. The cell below creates an array from a python list.
# **Task:** execute the cell. Notice the last line has only the `a` in it. This causes the value of `a` to be printed.

# In[6]:


l = [4,5,4,3,2,7]
a = np.array(l)
a


# Numpy arrays can be two-dimensional, three-dimensional, essentially any-dimensional. These are created from nested lists.
# 
# **Task:** execute the below cell. Notice that a square matrix is created.

# In[7]:


l = [[1,2,3],
     [4,5,6],
     [7,8,9]]
a = np.array(l)
a


# Numpy arrays can be two-dimensional, three-dimensional, essentially any-dimensional. These are created from nested lists.
# 
# **Task:** Extend the array a to be a 3x4 array with the numbers from 1-12 instead of 1-9.
# 
# Remeber you can use *variable*.shape to get the shape of an array/matrix.

# In[8]:


n = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

a = np.array(n)
a.shape



# ### 2.2 Random numbers
# 
# Numpy can do much more and we'll cover it in detail next week. For now, please take a moment to explore the generation of random numbers using the `numpy.random` module. 
# 
# The 'rand' function provides a single random numbers between 0 and 1. 
# 
# **Task:** execute the below cell a couple of times and observe that each number is random. 
# 
# **Task (for advanced students)**: Use the `?` method to find out what arguments the `rand()` function takes and explore the result. 

# In[9]:


np.random.rand()


# We will later use normally distributed numbers ("gaussian noise"). As you recall from your statistics courses, a normal distribution is characterised by its **mean** and **variance**.
# 
# The cell below creates an array of size 10 with mean 0.0 and variance 1.0.
# 
# **Task:** Run the cell below a couple of times and observe that the numbers generated are centered around 0.0, and that values close to 0.0 are more frequent than values larger than 1.0 or smaller than -1.0 .

# In[10]:


b = np.random.normal(0., 1., 10)
b


# What happens if we change the function call to 
# 
# np.random.normal(5., 1., 10), 
# 
# what if we call np.random.normal(0., 12., 10) 
# 
# or np.random.normal(0., 1., 50) instead? 
# 
# **Task:** First use the ? help functionality to investigate and then see if your answer is correct.

# In[11]:


np.random.normal(5., 1., 10)
#Do your investigations here


# In[12]:


np.random.normal(0., 12., 10) 


# In[13]:


np.random.normal(0., 1., 50)


# In[14]:


get_ipython().run_line_magic('pinfo', 'np.random.normal')


# ## 3 - Plotting with matplotlib
# 
# `matplotlib` is the de-facto standard tool for plotting in python. The essential functionality is contained in the `pyplot` submodule. Let's import it:

# In[15]:


import matplotlib.pyplot as plt


# By default, `matplotlib` opens a new window for each plot. Jupyter notebooks have special support for `matplotlib` so that it can display its plots inside the notebook, without creating a new window. This is activated by the following cell: 

# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ### 3.1 Plotting lines
# `matplotlib` can handle lists or arrays. Let's make a figure from a list:

# In[17]:


l = [4,3,6,5,4,7,3,5,3,4]
plt.plot(l)


# **Task**: Change the above cell to use an array for plotting. Create an array from the list as above, and passi this to the `plot` function. 

# In[18]:


l = [4,3,6,5,4,7,3,5,3,4]
a = np.array(l)
plt.plot(a)


# ### 3.2 Scatterplots - plotting point clouds
# 
# We will often plot "point clouds" with `matplotlib`, so-called scatterplots. Here, we will plot the distribution of a bivariate (i.e. 2-dimensional) point cloud distributed around 0.0 with variance 1.0 . 
# 
# The cell below creates a point cloud with 100 points using `numpy` random numbers. Note how we create two arrays using `numpy.random.normal`, one for `x` coordinates, and one for `y` coordinates. The point cloud is then plotted using the `scatter` function. 
# 
# **Task:** execute the cell multiple times and observe that the random points are different each time - because they're random. 
# 
# **Task (advanced):** Change the location shape of the point cloud by changing the mean and variance of `x` and `y` points.
# 
# **Task (advanced):** look up what `plt.gca()` is doing.

# In[19]:


cloud1_x = np.random.normal(0.0, .9, 100)
cloud1_y = np.random.normal(0.0, 1.0, 100)
ax = plt.scatter(cloud1_x, cloud1_y)
plt.gca().axis('equal')


# The `scatter` function lets you control the appearance of the points. For example, it can also plot red crosses instead of blue circles:

# In[20]:


plt.scatter(cloud1_x, cloud1_y, marker='+', c="green")


# ## 4 - Pandas and Data Frames 
# 
# The pandas module is dedicated to managing data. It is built around the `DataFrame` concept. A `DataFrame` is essentially a multidimensional array that supports textual identifiers for rows and columns. It can also mix different data types like numbers and strings, e.g. to add labels to data. 
# 
# The cell below imports pandas and create a `DataFrame` from our point cloud. Take a minute to observe that we first create a 2-dimensional array from `cloud1_x` and `cloud1_y`.
# 
# **Task:** run the cell below and observe that the `DataFrame` is nicely shown in tabular format. 

# In[21]:


import pandas as pd
cloud1_2dim = np.array([cloud1_x, cloud1_y])
df = pd.DataFrame(cloud1_2dim)
df


# Let's beautify this data Frame a little. First, we want to transpose it so that each point is a row, and columns correspond to coordinates. By convention, this is how multivariate data is stored. 
# 
# **Task:** run the cell below and observe that DataFrame is transposed, with two columns corresponding to two dimensions of the point cloud. 
# 
# **Note:** If you run the cell multiple times the `DataFrame` will transpose back and forth. Make sure the `DataFrame` is printed with 100 rows x 2 columns before continuing.

# In[22]:


df = df.transpose()
df


# A `DataFrames` supports naming columns and rows. It also allows adding new columns with per-point attributes. We will learn the nitty-gritty of this functionality later in this module. For now, the below code is provided that does the following:
# 1. name column zero "x" and column 1 "y"
# 2. name each point "cloud1_&lt;x>" where &lt;x> is a running index
# 3. add a common label "cloud1" to all points

# In[23]:


df.columns = ["x", "y"]
point_names = ["cloud1_{}".format(i) for i in range(len(cloud1_x))]
df.index = point_names
df['label'] = 'cloud1'
df


# Why, you may ask? What is this good for? 
# 
# Well, it is actually a very powerful feature for data analysis! The labels, point names, column names etc. allow to specify a way to select parts of the data frame, like all `x` coordinates:

# In[24]:


df['x']


# ... or the `y` coordinate of the point named `cloud1_3`:

# In[25]:


df.loc['cloud1_3',['y']]


# In[26]:


i = df.loc['cloud1_34':'cloud1_43',['x']]


# In[27]:


i


# In[28]:


i[i<0]


# **Task (advanced)**: write code that selects all `x` values less than zero, in the points labeled `cloud1_34` to `cloud1_43`.

# ## 5 - scikit-learn
# 
# The final part of today's practical is a look at the Scikit-learn module, a module for predictive data analysis. Scikit-learn contains tools for supervised and unsupervised learning for classification, regression, clustering, among other use cases. See the [scikit-learn home page](https://scikit-learn.org/stable/index.html) for more details!
# 
# For now we are interested in a simple classifier, the Naive Bayes classifier. It can be trained to separate classes of data points. For training, it takes examples of each class and estimates mean and variance of the associated coordinates (or *features*). The resulting parameters form the *model* of the Naive Bayes Classifier. 
# 
# Let's start by importing the Naive Bayes sub module from the scikit-learn module. In Python terms Scikit-learn is called `sklearn` and the naive bayes module `GaussianNB`. 

# In[29]:


from sklearn.naive_bayes import GaussianNB as nb


# Let's make some data for the classifier to classify. We use two point clouds, one with centered on [0.0,0.0] with variance 1.0 (as above), and a second onewith center [3.0, 3.0] and variance 1. 
# 
# **Task:** run the cell below. It creates two point clouds, stores each in a `DataFrame`, complete with labels and indices. 
# 
# **Note:** 
# The cell below creates a two-dimensional point cloud directly by using a two-dimensional center `[3.,3.]`. The `size` argument specifies that the resulting array should have 100 rows and 2 columns (`[100,1]`). We will cover these `numpy` features in the next unit. For now, it's ok to take the code as given.

# In[30]:


#create point clouds
cloud1 = np.random.normal([0.,0.], 1., size=[100,2])
cloud2 = np.random.normal([3.,3.], 1., size=[100,2])

#create DataFrame for first cloud
df1 = pd.DataFrame(cloud1, columns=['x', 'y'], index=["cloud1_{}".format(i) for i in range(len(cloud1))])
df1['label'] = 'cloud1'
                   
#create DataFrame for second cloud
df2 = pd.DataFrame(cloud2, columns=['x', 'y'], index=["cloud2_{}".format(i) for i in range(len(cloud2))]) 
df2['label'] = 'cloud2'
                   
df1


# In[31]:


df2


# Let's plot the two clouds. Conveniently, `pandas` has integrated matplotlib so that we can use the sophisticated data selection tools of a DataFrame for plotting. Again, this is mainly intended as a demonstration, we'll cover the details of what's going on below in a later unit.
# 
# **Task**: Run the cell below and observe how two point clouds are plotted. Can you identify the one with mean [0,0] and the one with mean [3,3]?
# 
# **Task (advanced students):** look up the documentation of `DataFrame.plot.scatter` and try to understand what's going on in the cell below. 

# In[32]:


plt.scatter(df1['x'], df1['y'], marker='o', c='blue')
plt.scatter(df2['x'], df2['y'], marker='x', c='red')


# **Task:** Create your own two clouds, one centered around 4,4 and one around 8,8. 
# 
# All the code but the actual creation of the clouds is given below, fill it out.

# In[33]:


#create point clouds
my_cloud1 = np.random.normal([4.,4.], 1., size=[100,2])
my_cloud2 = np.random.normal([3.,3.], 1., size=[100,2])

#create DataFrame for first cloud
df3 = pd.DataFrame(my_cloud1, columns=['x', 'y'], index=["my_cloud1_{}".format(i) for i in range(len(my_cloud1))])
df3['label'] = 'my_cloud1'
                   
#create DataFrame for second cloud
df4 = pd.DataFrame(my_cloud2, columns=['x', 'y'], index=["my_cloud2_{}".format(i) for i in range(len(my_cloud2))]) 
df4['label'] = 'my_cloud2'
                   
df3


# In[34]:


df4


# Now we have two point clouds, we can train the classifier to learn to separate them. 
# 
# Scikit-learn has a standardised way of training classifiers, using the `fit()` method. All we have to do is to give it data and labels. To make our life easier, we combine the two data frames:

# In[35]:


df_all = df1._append(df2)
df_all


# `df_all` now contains data from both point clouds, with the `label` column indicating which cloud each datapoint belongs to. 
# 
# The `label` column is now the label for training.
# 
# We can finally train the Scikit-learn classifier!

# In[36]:


from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X=df_all[['x','y']], y=df_all['label'])


# Finally, we need to check what the Naive Bayes classifier has learnt. To this end, we create a third point cloud with mean [1.5,1.5] and variance 1.5.  

# In[37]:


cloud3 = np.random.normal([1.5,1.5], 1.5, size=[100,2])
df3 = pd.DataFrame(cloud3, columns=['x', 'y'])


# This cloud sits right on top of the two existing clouds! Let's see how it looks like on top of the two existing clouds:

# In[38]:


plt.scatter(df1['x'], df1['y'], marker='o', c='blue')
plt.scatter(df2['x'], df2['y'], marker='x', c='red')
plt.scatter(df3['x'], df3['y'], marker='+', c='green')


# We're almost there! Now, let's use the trained Naive Bayes classifier to predict, for all points in cloud 3, which of the two original classes it is most likely to adhere to:

# In[39]:


label_pred = gnb.predict(df3[['x','y']])
label_pred


# Finally, we plot all points that belong to cloud one with light blue crosses, and those that belong to cloud2 with light red crosses.

# In[40]:


pred_cloud1 = df3.values[label_pred=='cloud1',:] #advanced array slicing, will be covered next week
pred_cloud2 = df3.values[label_pred=='cloud2',:] 

plt.scatter(df1['x'], df1['y'], marker='o', c='blue')
plt.scatter(df2['x'], df2['y'], marker='x', c='red')

plt.scatter(pred_cloud1[:,0], pred_cloud1[:,1], marker='+', c='lightblue')
plt.scatter(pred_cloud2[:,0], pred_cloud2[:,1], marker='+', c='pink')


# In[41]:


pred_cloud1 = df3.values[label_pred=='cloud1',:] #advanced array slicing, will be covered next week
pred_cloud2 = df3.values[label_pred=='cloud2',:] 

plt.scatter(df1['x'], df1['y'], marker='o', c='blue')
plt.scatter(df2['x'], df2['y'], marker='x', c='red')

plt.scatter(pred_cloud1[:,0], pred_cloud1[:,1], marker='+', c='lightblue')
plt.scatter(pred_cloud2[:,0], pred_cloud2[:,1], marker='+', c='pink')


# **Task (advanced):** change the distance, shape, and overlap of the point clouds by modifying the mean and the variance of the underlying normal distributions. How are the new points classified? What do you observe?

# ## 6 - Conclusion
# 
# That's it! In this notebook you have taken a tour around the most important data science tools in Python. 
# 
# ### 6.1 Check your learning!
# After having completed this session, you should:
# 1. Be familiar with running and operating Jupyter notebooks. 
# 2. have an understanding what numpy, matplotlib, pandas, and scikit-learn are doing. 
# 
# Next week we'll dive deep into Principal component analysis.
# 
# 
# 

# # Submission Instructions
# 
# Before submitting this via canvas please go to kernel -> 'Restart&Run All'. Please check afterwards if this introduced any issues, then you should fix them. Your notebook should, in the end always represent working code written in a linear way, one cell after the other.
