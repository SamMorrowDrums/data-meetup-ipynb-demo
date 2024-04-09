#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[1]:


import matplotlib.pyplot as plt

# Assuming you have a list of data called 'data'
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate the box and whisker plot
plt.boxplot(data)

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Box and Whisker Plot')

# Show the plot
plt.show()

