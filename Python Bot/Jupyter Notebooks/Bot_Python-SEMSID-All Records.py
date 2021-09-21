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
from collections import OrderedDict
import xlsxwriter
import dask.dataframe as dd
import numpy as np

column_name = ["SEMIS ID", "SEMIS ID (DC)", "SEMIS ID (M&E)", "Status"]

dict = {}

#data_f = pd.read_csv(r'E:/DGME/allteachers.csv', usecols = columns, low_memory=False)


# In[2]:


col_mm = ["School_SEMIS_Code", "School_Name", "Active_Ind"]
data_mm = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', usecols = col_mm , sheet_name="sheet")

data_mm = pd.DataFrame(data_mm)
data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]

data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)

data_mm.head()


# In[3]:


df_mm = data_mm[3000 :5000]
df_mm


# In[4]:



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


# ## Fetch All Records from Table

# In[52]:


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


# In[53]:


col_mm = ["School_SEMIS_Code", "School_Name", "Active_Ind"]
data_mm = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', usecols = col_mm , sheet_name="sheet")

data_mm = pd.DataFrame(data_mm)
data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]

data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)

data_mm.head()


# In[54]:


df_mm = data_mm[0 :5]
df_mm


# In[62]:


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


# In[32]:



# # ------------------------------------------------------------------
# import urllib3 as ul
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# url = "http://checker.sindheducation.gov.pk/CheckBiometrics.aspx"

# # create a new Chrome session
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver,10)

# # Search DDL
# search_ddl = driver.find_element_by_id("ContentPlaceHolder1_ddlSearchBy")
# select = Select(search_ddl)
# select.select_by_index(2)
# time.sleep(4)
# data = True
# j=0
# for index, row in df_mm.iterrows():
#     search_text = driver.find_element_by_id("ContentPlaceHolder1_txtSearch")
#     search_text.click()
#     search_text.clear()
#     search_text.send_keys(row['School_SEMIS_Code'])
#     search_text.send_keys(Keys.ENTER)
#     time.sleep(1)
#     search_button = driver.find_element_by_id("ContentPlaceHolder1_btn_search")
#     search_button.click()
#     time.sleep(1)

#     for k in wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[contains(@id,"eventHistoryTable")]//tr'))):
#         for i in range(0,15):
#             try:
#                 data_set = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gvDCDetails"]/tbody/tr['+str(k+1)+']/td['+str(i+1)+']')
#                 print(data_set)
#                 dict[column_name[i]] = data_set.get_attribute('innerText')  
#                 data = True    
#             except:
#                 data=False
#                 break
#         print(dict)
#         print("Record " + str(j) + ": Found")
#         if data:
#             with open(r'D:\RecordSet_Schoold.csv', 'a',newline='') as f_object:
#                 dictwriter_object = csv.DictWriter(f_object, fieldnames=column_name)
#                 if index==0:
#                     dictwriter_object.writeheader()
#                 dictwriter_object.writerow(dict)
#                 dict.clear()
#             j = j + 1
        
# driver.quit();
# print("Completed")


# In[ ]:


# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import pandas as pd

# # page = requests.get(url)
# # soup = BeautifulSoup(page.content, 'html.parser')
# # tables = soup.find_all("table")

# # table = tables[0]
# # tab_data = [[cell.text for cell in row.find_all(["th","td"])]
# #                         for row in table.find_all("tr")]
# # df = pd.DataFrame(tab_data)

# # df.columns = df.iloc[0,:]
# # df.drop(index=0,inplace=True)


# In[ ]:


#             html = urllib2.urlopen(url).read()
#             bs = BeautifulSoup(html)
#             table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="Table1") 
#             rows = table.findAll(lambda tag: tag.name=='tr')

    
#     http = ul.PoolManager()
#     response = http.request('GET', url)
#     soup = BeautifulSoup(response.data.decode('utf-8'))
# #     html = ul.request.urlopen(url).read()
# #     bs = BeautifulSoup(html)
#     table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="ContentPlaceHolder1_gvDCDetails") 
#     rows = table.findAll(lambda tag: tag.name=='tr')
#     print(rows)


# In[ ]:


import time
from selenium import webdriver

url = 'https://www.investing.com/economic-calendar/investing.com-eur-usd-index-1155'

driver = webdriver.Chrome()
driver.get(url)
item = driver.find_element_by_xpath('//*[contains(@id,"showMoreHistory")]/a')
driver.execute_script("arguments[0].click();", item)
time.sleep(2)
for table in driver.find_elements_by_xpath('//*[contains(@id,"eventHistoryTable")]//tr'):
    data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
    print(data)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.investing.com/economic-calendar/investing.com-eur-usd-index-1155'

driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver,10)

while True:
    try:
        item = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@id,"showMoreHistory")]/a')))
        driver.execute_script("arguments[0].click();", item)
    except Exception:break

for table in wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//*[contains(@id,"eventHistoryTable")]//tr'))):
    data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
    print(data)

driver.quit()

