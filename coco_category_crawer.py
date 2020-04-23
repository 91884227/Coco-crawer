#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
from tqdm import tqdm
import numpy as np
import itertools
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore")


# In[3]:


def URL_find_block(URL_, Max_):
    try:
        driver.get(URL_) 
        soup =  BeautifulSoup(driver.page_source)
        buf = soup.select(".col-md-4.col-xs-12.post-item")
        if( len(buf) > 0):
            print("iteration in %s" % URL_)
            for _ in tqdm(range(Max_)):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.5)

            soup =  BeautifulSoup(driver.page_source)
            buf = soup.select(".col-md-4.col-xs-12.post-item")
            print("length of  article in %s : %d" % (URL_, len(buf)))
        else:
            print("Nothing in %s" % URL_)
        
    except:
        print("error in block_get_title_data: %s" % URL_)
        
    return(buf)


# In[4]:


def block_get_title_data(block_):
    buf_title = "block_get_title_data---error---"
    buf_date = "block_get_title_data---error---"
    try:
        buf_title = block_.select(".post-title")[0].text
        buf_date = block_.select("li")[0].text
    except:
        print("error in block_get_title_data")
        #print(block_)
        
    return( (buf_title, buf_date) )


# In[5]:


def output_data(buf_):
    df = pd.DataFrame(buf_)
    df.columns = ["title", "date"]
    # delete some data
    df = df[df['title'] != "block_get_title_data---error---" ]
    name = "coco_title_category_%d_to_%d_MAX_%d.csv" % (START, END, MAX)
    df.to_csv(name, index = False, encoding= 'UTF-8')


# In[6]:


if __name__ == '__main__':
    START, END, MAX = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    #START, END, MAX = 1, 100, 2

    print("load webdriver...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    print("start get data from category %d to %d" % (START, END)) 
    list_URL = ["https://www.coco01.today/category/%d" % i for i in np.arange(START, END+1)]

    print("start to get all the block")
    buf = [ URL_find_block(i, MAX) for i in tqdm(list_URL)]
    list_block = list(itertools.chain(*buf))

    print("start to get title and data from block")
    buf = [ block_get_title_data(i) for i in tqdm(list_block)]

    try:
        output_data(buf)
        print("success to create file coco_title_category_%d_to_%d_MAX_%d.csv" % (START, END, MAX) )
    except:
        print("fail to create file " )
    
    driver.close()


# In[ ]:




