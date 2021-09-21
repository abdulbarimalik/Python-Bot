#!/usr/bin/env python
# coding: utf-8

# In[15]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
from selenium.webdriver.support.ui import Select
import time
import csv
from csv import DictWriter
from collections import OrderedDict
import xlsxwriter
import dask.dataframe as dd

column_name = ["CNIC", "Status"]
columns = ["CNIC", "Active_ind","Cadre"]
dict = {}

data_f = pd.read_csv(r'E:/DGME/allteachers.csv', usecols = columns, low_memory=False)


# In[16]:


data_f = pd.DataFrame(data_f)
data_f = data_f.loc[data_f['Active_ind']=='TRUE']
data_f = data_f[1100:1500]
                
url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(1)
time.sleep(4)
data = True
i = 0
for index, row in data_f.iterrows():
    search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
    search_text.click()
    search_text.clear()
    search_text.send_keys(row['CNIC'])
    search_text.send_keys(Keys.ENTER)
    time.sleep(1)
    search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
    search_button.click()
    time.sleep(6)

    try:
        data_set = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = data_set.get_attribute('innerText')
        print("Record " + str(i) + ": Matched")
        # data = True
    except:
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = 'Unmatched'
        print("Record " + str(i) + ": Not Found/Unmatched")
        # data = False
        # break
     
    with open(r'D:\Status_ActiveIndicators_Complete.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()
    i = i + 1;
driver.quit();
print("Completed")


# In[8]:


#data_f[data_f['CNIC'] == 4130351972391]


# In[ ]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import os
from selenium.webdriver.support.ui import Select
import time
import csv
from csv import DictWriter
from collections import OrderedDict
import xlsxwriter
import dask.dataframe as dd

col_sg  = ["SCH_ID", "SCH_NAME","STATUS"]
col_mm = ["School_ID","School_SEMIS_Code","School_Name","Active_Ind"']
dict = {}

data_f = pd.read_excel(r'E:/DGME/MNE_Schools.csv', usecols = columns, low_memory=False)


# In[ ]:


data_f = pd.DataFrame(data_f)
data_f = data_f.loc[data_f['Active_ind']=='TRUE']
data_f = data_f[1100:1500]
                
url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(1)
time.sleep(4)
data = True
i = 0
for index, row in data_f.iterrows():
    search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
    search_text.click()
    search_text.clear()
    search_text.send_keys(row['CNIC'])
    search_text.send_keys(Keys.ENTER)
    time.sleep(1)
    search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
    search_button.click()
    time.sleep(6)

    try:
        data_set = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = data_set.get_attribute('innerText')
        print("Record " + str(i) + ": Matched")
        # data = True
    except:
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = 'Unmatched'
        print("Record " + str(i) + ": Not Found/Unmatched")
        # data = False
        # break
     
    with open(r'D:\Status_ActiveIndicators_Complete.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()
    i = i + 1;
driver.quit();
print("Completed")

