#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[18]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[19]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[20]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[21]:


slide_elem.find('div', class_='content_title')


# In[22]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[24]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[26]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[27]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[28]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[29]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[30]:


df.to_html()


# In[31]:


browser.quit()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[32]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[38]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemisphere_parsing_tool = soup(browser.html, 'html.parser')

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for result in hemisphere_parsing_tool.find_all('div', class_='description'):
    
    hemispheres = {}
    
    browser.visit(url+result.a['href'])
    hemisphere_parsing_tool = soup(browser.html, 'html.parser')
    
    title = hemisphere_parsing_tool.find('div', class_="cover").h2.get_text()
    hemispheres["title"] = title

    browser.find_by_css('a.product-item h3').click()
    
    img_url = hemisphere_parsing_tool.find('li').a['href']
    
    hemispheres["img_url"] = f'https://marshemispheres.com/{img_url}'
   
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()
    


# In[39]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[40]:


# 5. Quit the browser
browser.quit()


# In[ ]:




