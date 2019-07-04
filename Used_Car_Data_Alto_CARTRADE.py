#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
from bs4 import BeautifulSoup
import requests


# In[4]:


url="https://www.cartrade.com/buy-used-cars/mumbai/hyundai/elite-i20/3881734.html"


# In[5]:


response=requests.get(url)
response.text


# In[6]:


soup= BeautifulSoup(response.text,"html.parser")


# In[7]:


for carname in soup.find_all("h1"):
    car=carname.text
    print(car)
    #print(type(car))
    brand=car.split(" ")
    
    brandName=str(brand[0])
    print(brandName)
    
    variant = ' '.join(brand[1:])
    print(variant)
    #print(type(variant))


# In[8]:


# this is for price
price1=[]

for div in soup.find_all("div",{"class":"wrapper v_content"}):
    #print(div)
    for div2 in div.find_all("div",{"class":"v_details"}):
        #print(div2)
        for div3 in div2.find_all("div",{"class":"pull-left"}):
            #print(div3)
            for span in div3.find_all("span"):
                  price1.append(span.text)
price2= price1[0:2]
price = ''.join(price2)
price


# In[9]:


data=[]
for div in soup.find_all("div",{"class":"widgetBox"}):
    #print(div)
    for table in div.find_all("table",{"class":"v_table"}):
        #print(table)
        for tr in table.find_all("tr"):
            #print(tr.text)
            for td in tr.find_all("td"):
                #print(td.text)
                data.append(td.text)
    
# printing the elements in list
#print(data)
city=str(data[1])
fuel=str(data[3])
year=str(data[17])
mileage=str(data[5])
print(city,fuel,year,mileage)


# In[10]:


Url=url.rpartition("buy")[0]
#Url
Site=Url.split(".")[1]
Site


# In[11]:


import xlsxwriter


# In[12]:


workbook=xlsxwriter.Workbook('Used_Car_Data_Alto.xlsx')
worksheet=workbook.add_worksheet()


# In[15]:


row=2
column=3
#conten=["Column_Name","S.No","Car","Brand","Model","Variant","Fuel Type","Model Year","Mileage","Price","City","Site","Url"]
actualdata=["Description",2,car,brandName,variant,variant,fuel,year,mileage,price,city,Site,Url]


# In[16]:


for items in actualdata:
    print(items)
    #worksheet.write(row,column,items)
    #row+=1
#workbook.close()


# In[ ]:




