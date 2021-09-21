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


# ### Record Matching using NIC/Personnel ID

# In[45]:


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

column_name = ["CNIC", "Employee_Code", "Employee_Name", "SEMID ID (DC)", "SEMIS ID (M&E)", "Status"]
columns = ["CNIC", "Employee_Code", "Employee_Name"]
dict = {}

data = pd.read_csv(r'E:/DGME/work/seld emp/all_employees.csv', usecols = columns, low_memory=False)


# In[47]:


data_f = pd.DataFrame(data)
#data_f = data_f.loc[data_f['Active_ind']=='TRUE' ]
data_f['CNIC'] = data_f['CNIC'].astype(pd.Int64Dtype())
data_f['CNIC'].dtype
data_f = data_f[30:34]
data_f = data_f.fillna(0)
data_f


# In[ ]:





# In[48]:


url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
# search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
# select = Select(search_ddl)
# select.select_by_index(1)
time.sleep(4)
data = False
i = 0
for index, row in data_f.iterrows():
    search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
    select = Select(search_ddl)
    select.select_by_index(1)
    time.sleep(4)
    search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
    search_text.click()
    search_text.clear()
    search_text.send_keys(row['CNIC'])
    search_text.send_keys(Keys.ENTER)
    time.sleep(1)
    search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
    search_button.click()
    time.sleep(1)
    try:
        data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = data_set.get_attribute('innerText')
        print("Record " + str(i) + ": Found")
        time.sleep(6)       
    except:
        search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
        select = Select(search_ddl)
        select.select_by_index(0)
        time.sleep(4)
        search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
        search_text.click()
        search_text.clear()
        if(row['Employee_Code']!=0):
            try:    
                search_text.send_keys(row['Employee_Code'])
                search_text.send_keys(Keys.ENTER)
                time.sleep(1)
                search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
                search_button.click()
                data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
                name =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[2]')
                semid_dc =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[9]')
                semid_me =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[12]')
                semid_sg = semid_dc.get_attribute('innerText')
                semid_mm = semid_me.get_attribute('innerText')
                status = data_set.get_attribute('innerText')
                emp_name = name.get_attribute('innerText')
                dict[column_name[0]] = row['CNIC']
                dict[column_name[1]] = row['Employee_Code']
                dict[column_name[2]] = emp_name
                dict[column_name[3]] = semid_sg
                dict[column_name[4]] = semid_mm
                dict[column_name[5]] = status
                print("Record " + str(i) + ": Found")
                time.sleep(6)
            except:
                dict[column_name[0]] = row['CNIC']
                dict[column_name[1]] = row['Employee_Code']
                dict[column_name[5]] = 'Not Found'
                print("Record " + str(i) + ": Not Found")  
                
        else:
            dict[column_name[0]] = row['CNIC']
            dict[column_name[1]] = row['Employee_Code']
            dict[column_name[5]] = 'Not Found'
            print("Record " + str(i) + ": Not Found")            
    with open(r'D:\Emp_Status.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()
    i = i + 1;
driver.quit();
print("Completed")            
                  



# In[ ]:


# url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# # create a new Chrome session
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# driver.implicitly_wait(5)


# # Search DDL
# # search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
# # select = Select(search_ddl)
# # select.select_by_index(1)
# time.sleep(4)
# data = False
# i = 0
# for index, row in data_f.iterrows():
#     search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
#     select = Select(search_ddl)
#     select.select_by_index(1)
#     time.sleep(4)
#     search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
#     search_text.click()
#     search_text.clear()
#     search_text.send_keys(row['CNIC'])
#     search_text.send_keys(Keys.ENTER)
#     time.sleep(1)
#     search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#     search_button.click()
#     time.sleep(1)
#     try:
#         data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
#         dict[column_name[0]] = row['CNIC']
#         dict[column_name[1]] = data_set.get_attribute('innerText')
#         print("Record " + str(i) + ": Found")
#         time.sleep(6)       
#     except:
#         search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
#         select = Select(search_ddl)
#         select.select_by_index(0)
#         time.sleep(4)
#         search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
#         search_text.click()
#         search_text.clear()
#         if(row['Employee_Code']!=0):
#             try:    
#                 search_text.send_keys(row['Employee_Code'])
#                 search_text.send_keys(Keys.ENTER)
#                 time.sleep(1)
#                 search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#                 search_button.click()
#                 data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
#                 name =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[2]')
#                 semid_dc =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[9]')
#                 semid_me =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[12]')
#                 semid_sg = semid_dc.get_attribute('innerText')
#                 semid_mm = semid_me.get_attribute('innerText')
#                 status = data_set.get_attribute('innerText')
#                 emp_name = name.get_attribute('innerText')
#                 dict[column_name[0]] = row['CNIC']
#                 dict[column_name[1]] = row['Employee_Code']
#                 dict[column_name[2]] = emp_name
#                 dict[column_name[3]] = semid_sg
#                 dict[column_name[4]] = semid_mm
#                 dict[column_name[5]] = status
#                 print("Record " + str(i) + ": Found")
#                 time.sleep(6)
#             except:
#                 dict[column_name[0]] = row['CNIC']
#                 dict[column_name[1]] = row['Employee_Code']
#                 dict[column_name[5]] = 'Not Found'
#                 print("Record " + str(i) + ": Not Found")  
                
#         else:
#             try:
#                 search_text.send_keys(row['Employee_Code'])
#                 search_text.send_keys(Keys.ENTER)
#                 time.sleep(1)
#                 search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#                 search_button.click()
#                 data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
#                 name =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[2]')
#                 semid_dc =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[9]')
#                 semid_me =  driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[12]')
#                 semid_sg = semid_dc.get_attribute('innerText')
#                 semid_mm = semid_me.get_attribute('innerText')
#                 status = data_set.get_attribute('innerText')
#                 emp_name = name.get_attribute('innerText')
                
#                 dict[column_name[0]] = row['CNIC']
#                 dict[column_name[1]] = row['Employee_Code']
#                 dict[column_name[2]] = emp_name
#                 dict[column_name[3]] = semid_sg
#                 dict[column_name[4]] = semid_mm
#                 dict[column_name[5]] = status
#                 print("Record " + str(i) + ": Found")
#                 time.sleep(6)
#             except:
#                 dict[column_name[0]] = row['CNIC']
#                 dict[column_name[0]] = row['Employee_Code']
#                 dict[column_name[1]] = 'Not Found'
#                 print("Record " + str(i) + ": Not Found")            
#     with open(r'D:\Check_Status.csv', 'a', newline='') as f_object:
#         dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
#         if index == 0:
#             dictwriter_object.writeheader()
#         dictwriter_object.writerow(dict)
#         dict.clear()
#     i = i + 1;
# driver.quit();
# print("Completed")            
                  



# In[ ]:


# data_f = pd.DataFrame(data_f)
# #data_f = data_f.loc[data_f['Active_ind']=='TRUE' ]
# # data_f = data_f[1100:1500]
                
# url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# # create a new Chrome session
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# driver.implicitly_wait(5)


# # Search DDL
# search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
# select = Select(search_ddl)
# select.select_by_index(1)
# time.sleep(4)
# data = False
# i = 0
# for index, row in data_f.iterrows():
#     search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
#     search_text.click()
#     search_text.clear()
#     search_text.send_keys(row['CNIC'])
#     search_text.send_keys(Keys.ENTER)
#     time.sleep(1)
#     search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#     search_button.click()
#     time.sleep(6)

#     try:
#         data_set = driver.find_element_by_xpath(
#             '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
#         dict[column_name[0]] = row['CNIC']
#         dict[column_name[1]] = data_set.get_attribute('innerText')
#         data = True
#         print("Record " + str(i) + ": Found")
        
#         if(data):
#             search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
#             select = Select(search_ddl)
#             select.select_by_index(0)
#             time.sleep(4)
#             search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
#             search_text.click()
#             search_text.clear()
#             search_text.send_keys(row['Employee_Code'])
#             search_text.send_keys(Keys.ENTER)
#             time.sleep(1)
#             search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#             search_button.click()
#             time.sleep(6)

#     #         try:
#             data_set = driver.find_element_by_xpath(
#                     '//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td[15]')
#             dict[column_name[0]] = row['Employee_Code']
#             dict[column_name[1]] = data_set.get_attribute('innerText')
#             print("Record " + str(i) + ": Found")      
#     #         except:

# #             dict[column_name[0]] = row['CNIC']
# #             dict[column_name[1]] = 'Not Found'
# #             print("Record " + str(i) + ": Not Found")
# #             break
#     except: 
#         # data = False
#         # break
#         dict[column_name[0]] = row['CNIC']
#         dict[column_name[1]] = 'Unmatched'
#         print("Record " + str(i) + ": Not Found/Unmatched")
#             # data = False
   

#     with open(r'D:\Check_Status.csv', 'a', newline='') as f_object:
#         dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
#         if index == 0:
#             dictwriter_object.writeheader()
#         dictwriter_object.writerow(dict)
#         dict.clear()
#     i = i + 1;
# driver.quit();
# print("Completed")


# In[ ]:




