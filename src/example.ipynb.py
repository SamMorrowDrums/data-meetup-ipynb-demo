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


# In[7]:


import requests
from ipython_secrets import *

# Set the API key and repository URL
api_key = get_secret('GITHUB_API_KEY')
repo_url = 'https://api.github.com/repos/OWNER/REPO'

# Set the headers with the API key
headers = {
    'Authorization': f'token {api_key}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make a GET request to the repository URL
response = requests.get(repo_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print the error message
    print(f'Request failed with status code {response.status_code}: {response.text}')

