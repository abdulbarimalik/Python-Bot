#!/usr/bin/env python
# coding: utf-8

# ### Import Packages

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
import numpy as np

column_name = ["SEMIS ID", "SEMIS ID (DC)", "SEMIS ID (M&E)", "Status"]

dict = {}


# #### Data Slicing/Filtering

# In[ ]:


col_mm = ["School_SEMIS_Code", "School_Name", "Active_Ind"]
data_mm = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', usecols = col_mm , sheet_name="sheet")

data_mm = pd.DataFrame(data_mm)
data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]

data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)

data_mm.head()


# In[ ]:


df_mm = data_mm[20000 :25000]
df_mm


# ### Get Selective Record Set

# In[ ]:



url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(2)
time.sleep(4)
data = True
i = 1
for index, row in df_mm.iterrows():
    for j in range(3):        
        search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
        search_text.click()
        search_text.clear()
        search_text.send_keys(row['School_SEMIS_Code'])
        search_text.send_keys(Keys.ENTER)
        time.sleep(1)
        search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
        search_button.click()
        time.sleep(6)
        break 

    try:
        data_set = driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
        semid_dc =  driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[9]')
        semid_me =  driver.find_element_by_xpath(
            '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[12]')
        semid_sg = semid_dc.get_attribute('innerText')
        semid_mm = semid_me.get_attribute('innerText')
        
        #if (semid_dc == semid_me ):
            
        dict[column_name[0]] = row['School_SEMIS_Code']
        dict[column_name[1]] = semid_sg
        dict[column_name[2]] = semid_mm
        dict[column_name[3]] = data_set.get_attribute('innerText')
        print("Record " + str(i) + ": Record Found")
        # data = True
    except:
        dict[column_name[0]] = row['School_SEMIS_Code']
        dict[column_name[3]] = 'Not Found'
        print("Record " + str(i) + ": Not Found")
        # data = False
        # break
    driver.implicitly_wait(3)
    with open(r'D:\SchoolsRecordSet_Status\Status_ActiveSchool_Recordset.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()
    i = i + 1;
    
driver.quit();
print("Completed")


# ### Get Complete Table

# In[ ]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import re
import os
from selenium.webdriver.support.ui import Select
import time
import csv
from csv import DictWriter
from collections import OrderedDict
import xlsxwriter
import dask.dataframe as dd
import numpy as np

#column_name = ["SEMIS ID", "SEMIS ID (DC)", "SEMIS ID (M&E)", "Status"]
column_name = ["Reg ID", "Emp. Name", "Fathers Name", "P.ID", "Gender", "Designation", "BPS", "Type", "SEMIS ID (DC)", "Inst. Name (DC)", "District (DC)", "SEMIS ID (M&E)", "Inst. Name (M&E)", "District (M&E)", "Status" ] 

dict = {}


# In[ ]:


col_mm = ["School_SEMIS_Code", "School_Name", "Active_Ind"]
data_mm = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', usecols = col_mm , sheet_name="sheet")

data_mm = pd.DataFrame(data_mm)
data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]

data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)

data_mm.head()


# In[ ]:


df_mm = data_mm[0 :5]
df_mm


# In[ ]:


import urllib3 as ul
from bs4 import BeautifulSoup
url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)

# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(2)
time.sleep(4)
data = True
j=0
for index, row in df_mm.iterrows():
    search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
    search_text.click()
    search_text.clear()
    search_text.send_keys(row['School_SEMIS_Code'])
    search_text.send_keys(Keys.ENTER)
    time.sleep(1)
    search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
    search_button.click()
    time.sleep(1)
    row_count = len(driver.find_elements_by_xpath("//*[@id='ContentPlaceHolder1_gvDCDetails']/tbody/tr"))
    print(row_count)
    #column_count = len(driver.find_elements_by_xpath("//table[@id='DataTable']/tbody/tr/td"))
    #break
    for k in range(1,row_count):
        for i in range(0,15):
            try:
                data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr['+str(k+1)+']/td['+str(i+1)+']')
                dict[column_name[i]] = data_set.get_attribute('innerText')  
                data = True    
            except:
                data=False
                break
        print(dict)        
        if data:
            with open(r'D:\RecordSet_Schoold.csv', 'a',newline='') as f_object:
                dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
                if index==0:
                    dictwriter_object.writeheader()
                dictwriter_object.writerow(dict)
                dict.clear()
        j = j + 1
driver.quit();
print("Completed")

# ------------------------------------------------- #

# ### Get Records from JSON/HTML

# In[ ]:


import pandas as pd
import numpy as np
import requests
import json
import csv
from pandas.io.json import json_normalize

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"
response = urlopen(url)
data = response.read().decode("utf-8")
dic = json.loads(data)

# now we will open a file for writing 
data_file = open('D:/data_file.csv', 'a'  , newline='') 
# create the csv writer object 
csv_writer = csv.writer(data_file) 
# Counter variable used for writing  
# headers to the CSV file 
count = 0
# employee_data = dic['emp_details'] 
for emp in dic: 
    if count == 0: 
        # Writing headers of CSV file 
        header = emp.keys() 
        print(header)
        csv_writer.writerow(header) 
        count += 1
    body  = emp.values()
    print(body)
    # Writing data of CSV file 
    csv_writer.writerow(emp.values())   

# save in JSON form for later use
with open('D:/person_list.json', 'w') as f:
    json.dump(dic, f)        
data_file.close()    


