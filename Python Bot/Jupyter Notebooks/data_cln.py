#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np


# ### SCH INFO

# In[32]:


col_sg  = ["SCH_ID", "SCH_NAME","STATUS"]
col_mm = ['School_SEMIS_Code', 'School_Name', 'Active_Ind']


# ##### MM SCH TABLE

# In[33]:


data_mm = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', usecols = col_mm , sheet_name="sheet")
data_mm = pd.DataFrame(data_mm)


# In[34]:


data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]
data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)


# ##### SG SCH TABLE

# In[35]:


data_sg = pd.read_excel(r'E:/DGME/work/Sindh_Schools_new (10-Mar-2021).xlsx', usecols = col_sg)


# In[36]:


data_sg['SCH_ID'].dtype


# In[7]:


# mergedStuff = pd.merge(data_sg, data_mm, on=['SCH_ID'], how='inner')
# mergedStuff.head()


# In[102]:


# mergedDF = pd.merge(data_mm, data_sg, left_on=['School_SEMIS_Code'], right_on=['SCH_ID'], how='inner')
# mergedDF.head()
# mergedDF


# In[42]:


# data_mm.where(data_mm.School_SEMIS_Code==data_sg.SCH_ID).notna()
# mergedDF = pd.merge(data_mm, data_sg, left_on=['School_SEMIS_Code','School_Name'], right_on=['SCH_ID','SCH_NAME'], how='inner')
# mergedDF.head()
# mergedDF


# In[37]:


# data_mm = data_mm.rename(columns={"School_SEMIS_Code": "SCH_ID", "School_Name": "SCHOOL_NAME", "Active_Ind":"ACTIVE_IND"})
# data_mm


# ##### Merge Tables

# In[39]:


mergedDF = pd.merge(data_mm, data_sg, left_on=['School_SEMIS_Code'], right_on=['SCH_ID'], how='inner')
mergedDF.head()
mergedDF


# In[ ]:





# In[65]:


mergedDF = pd.merge(data_mm, data_sg, on=['SCH_ID'], how='inner')
mergedDF.head()
mergedDF


# In[66]:


mergedDF  = mergedDF[mergedDF["STATUS"]!="Closed Permanent"]
mergedDF


# In[69]:


mergedDF.to_csv("E:/DGME/work/merged_DF.csv")


# In[70]:


mergedDF = pd.merge(data_mm, data_sg, left_on=['SCH_ID','SCHOOL_NAME'], right_on=['SCH_ID','SCH_NAME'], how='inner')
mergedDF.head()
mergedDF


# In[71]:


mergedDF  = mergedDF[mergedDF["STATUS"]!="Closed Permanent"]
mergedDF


# ### EMP INFO

# In[21]:


import pandas as pd
import numpy as np


# In[22]:


col_seld  = ["employee_personnel_id", "employee_name", "employee_cnic"]
col_mne = ["Employee_Code", "Employee_Name", "CNIC", "Active_Ind"]


# In[64]:


data_mne = pd.read_csv(r'E:/DGME/work/seld emp/mne_employees.csv', usecols = col_mne, encoding= 'unicode_escape')
data_mne = pd.DataFrame(data_mne)
data_mne


# In[28]:


data_mne['Active_Ind']


# In[48]:


data_mne[data_mne['Active_Ind'] =="TRUE"].count()


# In[54]:


data_mne[data_mne['Active_Ind'] =="FALSE"].count()


# In[55]:


data_mne[data_mne['Active_Ind'] ==1].count()


# In[56]:


data_mne[data_mne['Active_Ind'] ==0].count()


# In[49]:


df_mne = data_mne.loc[data_mne['Active_Ind'] =="TRUE"]
df_mne


# In[50]:


df_mne = data_mne.loc[data_mne['Active_Ind'] ==1]
df_mne


# In[52]:


df_mne = data_mne.loc[data_mne['Active_Ind'] =="FALSE"]
df_mne


# In[57]:


df_mne = data_mne.loc[data_mne['Active_Ind'] ==0]
df_mne


# In[59]:


df_mne = data_mne.loc[(data_mne['Active_Ind'] =="TRUE") | (data_mne['Active_Ind'] ==1) ]
df_mne
#data_mm = data_mm[0:100]
# df_mne['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
# data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
# print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)


# In[ ]:





# In[60]:


data_seld = pd.read_csv(r'E:/DGME/work/seld emp/seld_employee.csv', usecols = col_seld, encoding= 'unicode_escape')
data_seld = pd.DataFrame(data_seld)
data_seld


# In[61]:


mdf_cnic = pd.merge(df_mne, data_seld, left_on=['CNIC'], right_on=['employee_cnic'], how='inner')
mdf_cnic.head()
mdf_cnic


# In[63]:


mdf_eid = pd.merge(df_mne, data_seld, left_on=['Employee_Code','CNIC'], right_on=['employee_personnel_id','employee_cnic'], how='inner')
mdf_eid.head()
mdf_eid


# ##### DATA CLEANING

# In[74]:


mergedDF.SCH_NAME.dtype


# In[19]:


import pandas as pd
import numpy as np
from html2json import collect
import requests
import json


# 
# jsonD = json.dumps(htmlContent.text) converts the raw HTML content into a JSON string representation. 
# jsonL = json.loads(jsonD) parses the JSON string back into a regular string/unicode object. This results in a no-op, as any escaping done by dumps() is reverted by loads(). jsonL contains the same data as htmlContent.text.
# 
# Try to use json.dumps to generate final JSON instead of building the JSON by hand:

# In[25]:


url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"
htmlContent = requests.get(url, verify=False)
# ContentUrl = json.dumps({
#     htmlContent.text
# })
jsonD = json.dumps(htmlContent.text)
jsonL = json.loads(jsonD)
with open('E:/data.json', 'w', encoding='utf-8') as f:
    json.dump(htmlContent.text, f, ensure_ascii=False, indent=4)

# f = open("E:/demofile2.csv", "a")
# f.write(jsonL)
# f.close()
# data = htmlContent.text
# jsonD = json.dumps(htmlContent.text)
# jsonL = json.loads(jsonD)

#df = pd.DataFrame(list(my_dict.items()),columns = ['column1','column2'])
# df = pd.DataFrame.from_dict(employee_parsed.items())
# df
#print(df.to_string(index=False))

#ContentUrl='{ \"url\" : \"'+str(urls)+'\" ,'+"\n"+' \"uid\" : \"'+str(uniqueID)+'\" ,\n\"page_content\" : \"'+jsonL+'\" , \n\"date\" : \"'+finalDate+'\"}'


# In[11]:



# jfile = json.dumps(jsonL)

# with open('E:/data.json', 'w', encoding='utf-8') as f:
#     json.dump(jfile, f, ensure_ascii=False, indent=4)


# In[12]:


#print(jsonL)
# import json

# import csv
url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"
htmlContent = requests.get(url, verify=False)
# ContentUrl = json.dumps({
#     htmlContent.text
# })
jsonD = json.dumps(htmlContent.text)

jsonL = json.loads(jsonD)
# with open('E:/data.json', 'w', encoding='utf-8') as f:
#     json.dump(htmlContent.text, f, ensure_ascii=False, indent=4)


employee_parsed = json.loads(jsonL)

# emp_data = employee_parsed['page_content']

# # open a file for writing

# employ_data = open('E:/EmployData.csv', 'w')

# # create the csv writer object

# csvwriter = csv.writer(employ_data)

# count = 0

# for emp in emp_data:

#       if count == 0:

#              header = emp.keys()

#              csvwriter.writerow(header)

#              count += 1

#       csvwriter.writerow(emp.values())

# employ_data.close()
# # f = open("E:/demofile2.csv", "a")
# # f.write(jsonL)
# # f.close()


# In[ ]:





# In[13]:


# import html2json

# html2json.collect(jsonL,)


# ##### JSON to CSV

# In[14]:


import pickle


# In[17]:


# import pickle
# url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"
# htmlContent = requests.get(url, verify=False)
# ContentUrl = json.dumps({
#     htmlContent.text
# })
#Here's an example dict
(#grades, =, {, 'Alice':, 89,, 'Bob':, 72,, 'Charles':, 87, })

#Use dumps to convert the object to a serialized string
# serial_emp = pickle.dumps( ContentUrl )

# #Use loads to de-serialize an object
# received_grades = pickle.loads( serial_emp )


# In[ ]:


print(received_grades)


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

url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
emp_list = driver.find_element_by_tag_name('body')
# df  = pd.read_html("http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1")
# select.select_by_index(1)
# time.sleep(4)
# data = True


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
(#, df, =, pd.read_html("http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"))

url = "http://checker.sindheducation.gov.pk:78/WebApplication1/Home/GetPage/?token=ztiGer000&pid=1"

# create a new Chrome session
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.implicitly_wait(5)


# Search DDL
emp_rec = driver.find_element_by_tag_name('body').get_attribute('innerText')
# df  = pd.read_html(emp_list)
jsonD = json.dumps(emp_rec)
jsonL = json.loads(jsonD)
# print(emp_list)


# In[ ]:


# tbl = driver.find_element_by_xpath("//html/body/main/article/section[2]/div/article/table").get_attribute('outerHTML')

# df  = pd.read_html(tbl)


# #### SELD Employee

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


# In[3]:


teaching_staff = pd.read_csv("E:/DGME/DGME School Record set/seld_employee.csv")
teaching_staff[0:10]


# In[10]:


teaching_staff.info()


# In[15]:


teaching_staff.count()


# In[16]:


len(teaching_staff.index)


# In[19]:


teaching_staff.nunique()


# In[30]:


print(teaching_staff.duplicated().sum())


# #### MNE SCH ANALYSIS

# In[86]:


import pandas as pd
import numpy as np


# In[89]:


data = pd.read_excel(r'E:/DGME/work/MNE_Schools.xlsx', sheet_name="sheet")


# #### ANALYSIS ON FULL DATA SET

# In[90]:


df_cmp = pd.DataFrame(data)
#df_cmp = df_cmp.fillna(0)
df_cmp['School_SEMIS_Code'] = df_cmp['School_SEMIS_Code'].astype(np.int64)
df_cmp['Active_Ind'] = df_cmp['Active_Ind'].astype(np.int64())
print(df_cmp['School_SEMIS_Code'].dtype, df_cmp['Active_Ind'].dtype)


# In[91]:


df_cmp.info()


# In[92]:


df_cmp.count()


# In[ ]:





# #### ACTIVE SCHOOLS

# In[76]:


data_mm = pd.DataFrame(data)
data_mm = data_mm.loc[data_mm['Active_Ind']==1]
#data_mm = data_mm[0:100]
data_mm['School_SEMIS_Code'] = data_mm['School_SEMIS_Code'].astype(np.int64)
data_mm['Active_Ind'] = data_mm['Active_Ind'].astype(np.int64())
print(data_mm['School_SEMIS_Code'].dtype, data_mm['Active_Ind'].dtype)


# In[64]:


data_mm.count()


# In[ ]:





# In[65]:


data_mm.info()


# In[95]:


import psycopg2


# #### Connection with Postgres DB

# In[99]:


connection = psycopg2.connect(user="postgres",
                                                      password="123456",
                                                      host="localhost",
                                                      port="5432",
                                                      database="postgres")
cursor = connection.cursor()


# In[101]:


try:
#     postgres_insert_query = """ INSERT INTO air_data (supplier_name_out,departure_time_out
#                                                   ,arrival_time_out,departure_airport_out,arrival_airport_out,flight_duration_out,stay_out,supplier_name_in,
#                                                   departure_airport_in,arrival_airport_in,departure_time_in,arrival_time_in,
#                                                   flight_duration_in,stay_in,fare,travel_date_out,travel_date_in,cabin,destination,source) VALUES
#                                                   (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#     record_to_insert = (
#                             travel_agent_out, dep_time_out, arr_time_out,dep_air_out,arr_air_out, flight_dur_out, flight_stay_out,
#                             travel_agent_in, dep_air_in, arr_air_in,dep_time_in, arr_time_in, flight_dur_in,
#                             flight_stay_in, fare_travel, b.strftime("%y/%m/%d"), a.strftime("%y/%m/%d"),
#                             c,'Thiruvananthapuram', 'SkyScanner')
    postgres_insert_query = """ INSERT INTO seld_employee VALUES(1,'Karachi Central','Liaqatabad Town','45-Hadi Market','408150223','GGHS','ISHATUL QURAN',NULL,'School'
                                ,NULL,NULL,'ZUBEDA SIBTAY','SIBTAY HASAN','4210107287432','F',NULL,'7/26/1957 7:00:00 PM','B.A',NULL,NULL,'10065230','H.M','17','9/30/1984 7:00:00 PM',NULL,'Non-Teaching'
                                ,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,'Karachi',NULL,1,'7/25/2017 7:00:00 PM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
                             """
    cursor.execute(postgres_insert_query)

    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into scrapped data table")

except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into mobile table", error)


# #### Connection with Postgres

# In[98]:


try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432",
                                  database="DGME_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


# In[ ]:




