import requests
import string
import pandas as pd
from bs4 import BeautifulSoup , SoupStrainer
import re
from HtmlTableParser import HTMLTableParser

#df = pd.read_csv('/home/sukumar/Desktop/objective/Inputcsv.csv')

r=requests.get("https://www.sec.gov/Archives/edgar/data/35315/0000035315-03-000001.txt")
#print(r.content)
soup=BeautifulSoup(r.content)


#print(soup.prettify())

df=pd.read_csv('/home/sukumar/Desktop/objective/Inputcsv.csv')


onlyOne=df[df['Filename'].str.contains("0000035315-03-000001")]



def getTableData(datatable):
    list=[]
    count=0
    rows = datatable.findChildren(['tr'])

    for row in rows:
        count=count+1
        cells = row.findChildren('td')
        if len(cells) == 6:
         for cell in cells:
            ps = cell.findChildren('p')
            for p in ps:
                #for data in td
                tdData=p.find('font')
                if True:
                 clean1=string.replace(str(tdData), '<font size="-2">', '')
                 clean2 = string.replace(str(clean1), '</font>', '')
                 clean3=string.replace(str(clean2), '<br/>', '')
                 print("selected values", clean3)
                 list.append(clean3)
    return list


for table in soup.find_all("table"):
         rows = table.findChildren(['tr'])
         for row in rows:
            cells = row.findChildren('td')
            for cell in cells:
               ps = cell.findChildren('p')
               for p in ps:
                   bs=p.findChildren('b')
                   for b in bs:
                    font=b.findChildren('font')
                    for f in font:
                        if "Credit Default Swap" in f:
                         with open("/home/sukumar/PycharmProjects/Objective/output1.txt", "w") as file:
                          file.write(str(table))
                         l= getTableData(table)
                         print(l)
                         for i in range(len(l)):
                             onlyOne["Attribute"]=l[i]
                             if i<=3:
                              df["Values"] = l[i+4]




print(df)
df.to_csv("outPut.csv")

#df.to_csv("outPut.csv")