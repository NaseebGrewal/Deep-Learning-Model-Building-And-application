#!/usr/bin/env python
# coding: utf-8

# # Lesson 4: Installing packages

# In this lesson, you will learn how to install third-party packages using a command called `pip`.
# 
# Once you have installed a package, you can use functions from the package by importing them using the `import` command.

# ## Installing packages using `pip`

# Run the cell below to install the `bs4` package:

# In[ ]:


get_ipython().system('pip install bs4')


# **Note:** You can safely ignore any warnings you see about upgrading pip.

# bs4 is short for **Beautiful Soup 4**. You can check out the [Beautiful Soup documentation](https://pypi.org/project/beautifulsoup4/) if you want to learn more about the package, but it gives you tools to interpret HTML webpages inside Python programs.
# 
# Now that you have installed the bs4 package, you can use it in your programs!
# 
# First, you need to import the `BeautifulSoup` function you'll use from the `bs4` package, as well as some other packages:

# In[ ]:


from bs4 import BeautifulSoup

import requests # let's you download webpages into python
from helper_functions import * 
from IPython.display import HTML, display


# ## Get data from the web
# 
# In this section, you'll "scrape", or download HTML data from a website, in this case from a [Batch newsletter](https://www.deeplearning.ai/the-batch/) published by DeepLearning.AI.
# 
# You'll use the `requests` Python package to download the data from the webpage and make it available in your program:

# In[ ]:


# The url from one of the Batch's newsletter
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

# Getting the content from the webpage's contents
response = requests.get(url)

# Print the response from the requests
print(response)


# **Note:** The `<Response [200]>` you see is an indication from the requests library that your HTTP request was successful. You can ask the chatbot for details about other codes you might see.

# Now that you have downloaded the content from the website, you can display it in the notebook using the following code:

# In[ ]:


HTML(f'<iframe src={url} width="60%" height="400"></iframe>')


# Next, you'll use Beautiful Soup to extract all the text paragraphs from the HTML structure that you retrieved, and save it as a single string. Here is the code to do this:

# In[ ]:


# Using beautifulsoup to extract the text
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the text in paragraph elements on the webpage
all_text = soup.find_all('p')

# Create an empty string to store the extracted text
combined_text = ""

# Iterate over 'all_text' and add to the combined_text string
for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

# Print the final combined text
print(combined_text)


# For more details about how this code works, you can ask the chatbot:

# <p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>:
# <br><br>
# What is the following code doing?
# <br><br>
# soup = BeautifulSoup(response.text, 'html.parser')<br>
# all_text = soup.find_all('p')
# </p>

# ## Extracting information from scraped website data using LLMs

# You can pass the text you just extracted from the Batch newsletter website to an LLM and ask it to extract the most relevant information for you.
# 
# Start by writing the prompt and passing in the text you extracted:

# In[ ]:


prompt = f"""Extract the key bullet points from the following text.

Text:
{combined_text}
"""


# Then pass the prompt to the LLM:

# In[ ]:


print_llm_response(prompt)


# ## One more example of installing packages
# 
# Throughout the courses so far, you've imported helper functions from a file called `helper_functions.py` using commands like `from helper_functions import get_llm_response`.
# 
# The DeepLearning.AI team has created a third-party package called `aisetup` that you can use to access the helper functions from the course in your own code outside of this learning platform.
# 
# To install it, run the following command:

# In[ ]:


get_ipython().system('pip install aisetup')


# Now the package is installed, you can import helper functions from it using the `import` command. For example, if you want to import `get_llm_response`, you now run this code:

# In[ ]:


from aisetup import get_llm_response


# In[ ]:


response = get_llm_response("Why is the programming language called Python?")

# Print LLMs response
print(response)


# ## Extra practice
# 
# Try the following exercises to test what you have learned. If you get stuck, as the chatbot for help!
# 
# ### Exercise 1
# 
# Modify the following code to answer the following question:
# - Who built the new short course mentioned in the letter?

# In[ ]:


# Modify the prompt
prompt = f"""YOUR PROMPT HERE

Text:
{combined_text}
"""
print_llm_response(prompt)


# ### Exercise 2
# 
# Use the `celsius_to_fahrenheit` function in the `aisetup` package to calculate the Fahrenheit equivalent of 0 degrees Celsius.
# 
# You'll need to complete the import statement and the calculation.

# In[ ]:


# Complete the import statement
from

# Complete the calculation
zero_celsius_in_fahrenheit =
print (zero_celsius_in_fahrenheit)


# ### Challenge exercise!
# 
# Write code that uses the `bs4` package to create a string that contains the **title element from the Batch newsletter**. This is the text that starts "The World Needs More Intelligence".
# 
# **Hint 1:** Titles on webpages are often header elements, with tags like `<h1>` or `<h2>`.
# **Hint 2:** Ask the chatbot for help, using the code you have already written as a starting point.

# In[ ]:


# Your code here

title =

print(title)

