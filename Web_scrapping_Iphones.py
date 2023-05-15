#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests


# In[1]:


url="https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[2]:


driver = webdriver.Chrome(executable_path=r'C:\Users\pavan\Desktop\business analytics\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(url)


# In[13]:


soup= BeautifulSoup(driver.page_source,'html.parser')


# # Next Page Links

# In[14]:


next_page_link=[]
next_page=soup.find_all('div',{'class':'_2MImiq'})
for i in next_page:
    a=i.find_all('nav',{'class':'yFHi8N'})
    for j in a:
        b=j.find_all('a',{'class':'ge-49M'})
        for k in b:
            next_page_link.append(k.get('href'))


# In[15]:


links=[]
for i in next_page_link:
    links.append('https://www.flipkart.com'+i)
links


# In[58]:


mega_links=[]
for i in range(1,10):
    mega_links.append('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+str(i))
mega_links


# # Mobile_name

# In[16]:


soup= BeautifulSoup(driver.page_source,'html.parser')
m_name=soup.find_all('div',{'class':'col col-7-12'})
len(m_name)


# In[17]:


mobile_name=[]
mobile_rating=[]
for q in links:
    driver.get(q)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    m_name=soup.find_all('div',{'class':'col col-7-12'})
    for i in m_name:
        a=i.find_all('div',{"class":"_4rR01T"})
        for j in a:
            mobile_name.append(j.text)

mobile_name


# In[18]:


len(mobile_name)


# # mobile_rating

# In[19]:


mobile_rating=[]
for q in links:
    driver.get(q)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    m_rating=soup.find_all('div',{'class':'gUuXy-'})
    for i in m_rating:
        a=i.find_all('span',{'class':'_1lRcqv'})
        for j in a:
            b=j.find_all('div',{'class':'_3LWZlK'})
            for k in b:
                mobile_rating.append(k.text)
mobile_rating


# In[20]:


len(mobile_rating)


# # proccessor

# In[27]:


jip=soup.find_all('div',{'class':'fMghEO'})
jip[0].text


# In[29]:


proccessor=[]
for q in links:
    driver.get(q)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    pro=soup.find_all('div',{'class':'fMghEO'})
    for i in pro:
        proccessor.append(i.text)
proccessor


# In[30]:


len(proccessor)


# # Phone_website

# In[31]:


phone_website=[]
for q in links:
    driver.get(q)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    p_web=soup.find_all('div',{'class':'_2kHMtA'})
    for i in p_web:
        a=i.find_all('a',{'class':'_1fQZEK'})
        for j in a:
            o=j.get('href')
            phone_website.append(o)
phone_website


# In[32]:


len(phone_website)


# # Mobile_Price

# In[33]:


mobile_price=[]
for q in links:
    driver.get(q)
    soup= BeautifulSoup(driver.page_source,'html.parser')
    m_price=soup.find_all('div',{'class':'_30jeq3 _1_WHN1'})
    for i in m_price:
        mobile_price.append(i.text)
mobile_price


# In[34]:


print(len(mobile_name))
print(len(mobile_rating))
print(len(proccessor))
# print(len(ram))
# print(len(camera_specification))
# print(len(Battery_specification))
print(len(phone_website))
print(len(mobile_price))


# In[35]:


dff1=pd.DataFrame(mobile_name,columns={'mobile_name'})
dff1.to_csv('dff1.csv')


# In[36]:


dff2=pd.DataFrame(mobile_rating,columns={'mobile_rating'})
dff2.to_csv('dff2.csv')


# In[37]:


dff3=pd.DataFrame(proccessor,columns={'proccessor'})
dff3.to_csv('dff3.csv')


# In[38]:


dff8=pd.DataFrame(phone_website,columns={'phone_website'})
dff8.to_csv('dff8.csv')


# In[39]:


dff9=pd.DataFrame(mobile_price,columns={'mobile_price'})
dff9.to_csv('dff9.csv')

