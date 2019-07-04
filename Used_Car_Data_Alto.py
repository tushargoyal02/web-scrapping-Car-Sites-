#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
from bs4 import BeautifulSoup
import requests


# In[2]:


#carName="Enter car name:"
#city=input("Enter city name, you wanna search car:")
#url = 'https://www.cars24.com/buy-used-hyundai-cars-'+city


# In[3]:


url="https://www.cars24.com/buy-used-Hyundai-Grand-i10-2015-cars-Jaipur-1078463111/"


# In[4]:


response=requests.get(url)


# In[5]:


response.text


# In[6]:


soup= BeautifulSoup(response.text,"html.parser")


# In[7]:


for carName in soup.find_all("h1",{"class":"d-inline _1bMVz"}):
    car=carName.text
    print(type(car))
    print(car)
    
    # printing the brand name for the car
    brand=car.split(" ")
    
    brandName=str(brand[0])
    #print(type(brandName))
    
    # getting the model variant
    
    
    variant = ' '.join(brand[1:])
    print(variant)
    #print(type(variant))
    
    


# In[8]:


# price
for h2 in soup.find_all("h2",{"class":"s5C1S"}):
    price="Rs:"+h2.text
    print(price)
    


# In[9]:


#new data list
dataSet=[]
for p in soup.find_all("p"):
    dataSet.append(p.text)

city=str(dataSet[1])
#print(type(city))
year=str(dataSet[4])
Mileage=str(dataSet[5])
fuelType=str(dataSet[6])


# In[10]:


Url=url.rpartition("buy")[0]
#print(type(Site))
Site=Url.split(".")[1]


# In[11]:


# importing files for Spreadsheet
import xlsxwriter


# In[12]:


workbook=xlsxwriter.Workbook('Used_Car_Data_Alto.xlsx')
worksheet=workbook.add_worksheet()


# In[ ]:





# In[13]:


row=2
column=1
conten=["Column_Name","S.No","Car","Brand","Model","Variant","Fuel Type","Model Year","Mileage","Price","City","Site","Url"]
actualdata=["Description",1,car,brandName,variant,variant,fuelType,year,Mileage,price,city,Site,Url]


# In[14]:


for item in conten:
    worksheet.write(row,column,item)
    row +=1
row1=2
column1=2
for items in actualdata:
    worksheet.write(row1,column1,items)
    row1+=1
workbook.close()


# In[ ]:





# In[ ]:




