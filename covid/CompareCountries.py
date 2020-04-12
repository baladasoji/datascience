#!/usr/bin/env python
# coding: utf-8

# In[1]:


# do the necesssary imports
import pandas as pd
import matplotlib.pyplot as plt
import datetime


# In[4]:


alldata=pd.read_csv("Enigma-JHU.csv", parse_dates=['last_update'])


# In[5]:


# Prepare a list of countries
countries=['India', 'Denmark','Sweden']


# In[7]:


# Split the data country wise and copy it into a list
ad=[]
for c in countries:
    ad.append(alldata.query('combined_key == @c'))


# In[10]:


# plot the confirmed cases
for data in ad:
    plt.plot(data.last_update, data.confirmed)
plt.legend(countries)
plt.savefig('confirmed.png');
plt.clf();

# In[8]:


# plot the deaths
for data in ad:
    plt.plot(data.last_update, data.deaths)
plt.legend(countries)
plt.savefig('deaths.png');
plt.clf();


# In[9]:


# plot the recovered
for data in ad:
    plt.plot(data.last_update, data.recovered)
plt.legend(countries)
plt.savefig('recovered.png');
plt.clf();

