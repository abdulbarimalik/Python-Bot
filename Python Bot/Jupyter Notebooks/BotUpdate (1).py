#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


column_name = ["Reg ID", "Emp. Name", "Fathers Name", "P.ID", "Gender", "Designation", "BPS", "Type", "SEMIS ID (DC)", "Inst. Name (DC)", "District (DC)", "SEMIS ID (M&E)", "Inst. Name (M&E)", "District (M&E)", "Status" ] 
column = ["CNIC"]
# Read Record Set
data_f = pd.read_csv(r'E:/DGME/allteachers.csv', usecols = column, low_memory=False)

dict = {}


# In[3]:


url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.29.0-win64/geckodriver.exe')
driver.get(url)
driver.implicitly_wait(5)

# read data_file
data_f = data_f[0:]
#data_f = data_f[0:100]
#data_f # 393025


# ##### Get & Push All Records

# In[4]:


# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(1)
time.sleep(4)
data = True
j=0
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
    for i in range(0,15):
        try:
            data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr[2]/td['+str(i+1)+']')
            dict[column_name[i]] = data_set.get_attribute('innerText')
            data = True
            
        except:
            data=False
            break
    if data:
        with open(r'D:\RecordSet_Complete.csv', 'a',newline='') as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
            if index==1:
                dictwriter_object.writeheader()
            dictwriter_object.writerow(dict)
            dict.clear()
    print("Record " + str(j) + ": Found")
    j = j + 1
        
driver.quit();
print("Completed")


# ##### Get and Push Selected Record Set

# In[10]:


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


column_name = ["CNIC", "Status"]

data_f = pd.read_csv(r'E:/DGME/records.csv')

dict = {}

url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.29.0-win64/geckodriver.exe')
driver.get(url)
driver.implicitly_wait(5)

# read data_file
#data_f = data_f[0:]
data_f = data_f[0:100]
data_f # 393025

# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(1)
time.sleep(4)
data = True
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
        # data = True
    except:
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = 'Unmatched'
        # data = False
        # break

    with open(r'D:\StatusReport.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()

driver.quit();
print("Completed")


# ##### Active Status Record Set

# In[12]:


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


#data_f = pd.read_excel(r'E:/DGME/allteachers.xlsx', usecols = columns)
# data_f[0:10]
chunksize = 10 ** 6
#for chunk in pd.read_csv(filename, chunksize=chunksize):
data_f = pd.read_csv(r'E:/DGME/allteachers.csv', usecols = columns, low_memory=False)
#data_f[0:50]


# In[13]:


data_f = pd.DataFrame(data_f)
data_f = data_f.loc[data_f['Active_ind']=='TRUE']
data_f = data_f[0:100]


# In[99]:


url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Firefox session
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.29.0-win64/geckodriver.exe')
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
select = Select(search_ddl)
select.select_by_index(1)
time.sleep(4)
data = True
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
        # data = True
    except:
        dict[column_name[0]] = row['CNIC']
        dict[column_name[1]] = 'Unmatched'
        # data = False
        # break

    with open(r'D:\StatusReport_Active.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()

driver.quit();
print("Completed")


# ##### Test Code

# In[17]:


data_f = pd.DataFrame(data_f)
data_f = data_f.loc[data_f['Active_ind']=='TRUE']
data_f = data_f[80:100]
                
url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# create a new Firefox session
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.29.0-win64/geckodriver.exe')
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
     
    with open(r'D:\Status_ActiveIndicators.csv', 'a', newline='') as f_object:
        dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
        if index == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow(dict)
        dict.clear()
    i = i + 1;
driver.quit();
print("Completed")


# In[107]:


# data_f = pd.DataFrame(data_f)
# data_f = data_f.loc[data_f['Active_ind']=='TRUE']
# data_f = data_f[0:10]
                
# url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# # create a new Firefox session
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # driver = webdriver.Firefox(executable_path='E:/geckodriver-v0.29.0-win64/geckodriver.exe')
# driver.get(url)
# driver.implicitly_wait(5)


# # Search DDL
# search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
# select = Select(search_ddl)
# select.select_by_index(1)
# time.sleep(4)
# data = True
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
#         print("Record " + str(i) + ": Matched")
#         # data = True
#     except:
#         dict[column_name[0]] = row['CNIC']
#         dict[column_name[1]] = 'Unmatched'
#         print("Record " + str(i) + ": Not Found/Unmatched")
#         # data = False
#         # break
     
#     with open(r'D:\Status_ActiveIndicators.csv', 'a', newline='') as f_object:
#         dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
#         if index == 0:
#             dictwriter_object.writeheader()
#         dictwriter_object.writerow(dict)
#         dict.clear()
#     i = i + 1;
# driver.quit();
# print("Completed")


# In[108]:



# f = open('E:/DGME/allteachers.csv', 'r')
# df = pd.DataFrame(file)
# df[0:10]
#f = open('E:/DGME/allteachers.csv', 'r')
# with f:

#     reader = csv.reader(f)

#     for row in reader:
#         for e in row:
#             print(e)
# file = csv.reader('E:/DGME/allteachers.csv')
# file
# df = pd.DataFrame(file)
# #data_f = df[df['Active_ind']=="TRUE"] 
# df[0:10]
# Read Record Set
#     # Open an Excel workbook
#     workbook = xlsxwriter.Workbook('D:\StatusReport.xlsx')
#     # Set up a format
#     c_format_1 = workbook.add_format(properties={'bold': True, 'font_color': 'green'})
#     c_format_2 = workbook.add_format(properties={'bold': True, 'font_color': 'red'})
    
#     # Create a sheet
#     worksheet = workbook.add_worksheet('status_report')
    
#     # Write the headers
#     for col_num, header in enumerate(column_name):
#         worksheet.write(0,col_num, str(header))
#     # Save the data from the OrderedDict into the excel sheet
#     for row_data in enumerate(zip(*dict)):
#         for cell_data in enumerate(row_data):
#             if cell_data ==  "Matched":
#                 worksheet.write(str(cell_data), c_format_1)
#             else:
#                 worksheet.write(str(cell_data), c_format_2)

#     # Close the workbook
#     workbook.close()


# In[ ]:




