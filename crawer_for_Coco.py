#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import requests
import numpy as np
from bs4 import BeautifulSoup
import itertools
import warnings
warnings.filterwarnings("ignore")
import sys
from tqdm import tnrange, tqdm_notebook, tqdm
import pandas as pd


# In[4]:


def URL_find_block(URL_):
    rs = requests.session()
    res = rs.get(URL_, verify = False)
    soup = BeautifulSoup(res.text)
    return(soup.select('.list-content.clearfix'))


# In[5]:


def block_get_title_data(block_):
    buf_title = "block_get_title_data---error---"
    buf_date = "block_get_title_data---error---"
    try:
        buf_title = block_.select(".post-title")[0].text
        buf_date = block_.select(".text")[1].text
    except:
        print("error in block_get_title_data")
        #print(block_)
        
    return( (buf_title, buf_date) )


# In[6]:


def output_data(buf_):
    df = pd.DataFrame(buf_)
    df.columns = ["title", "date"]
    # delete some data
    df = df[df['title'] != "block_get_title_data---error---" ]
    name = "coco_title_%d_to_%d.csv" % (START, END)
    df.to_csv(name, index = False, encoding= 'UTF-8')


# In[7]:


if __name__ == '__main__':
    START, END = int(sys.argv[1]), int(sys.argv[2])
    #START, END = 1, 63

    print("start get data from page %d to %d" % (START, END)) 
    list_URL = ["https://www.coco01.today/?page=%d&order=1" % i for i in np.arange(START, END+1)]

    print("start to get all the block")
    buf = [ URL_find_block(i) for i in tqdm(list_URL)]
    list_block = list(itertools.chain(*buf))

    print("start to get title and data from block")
    buf = [ block_get_title_data(i) for i in tqdm(list_block)]

    try:
        output_data(buf)
        print("success to create file coco_title_%d_to_%d.csv" % (START, END) )
    except:
        print("fail to create file " )

