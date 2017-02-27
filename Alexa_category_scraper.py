"""
Alexa Category Wise Scraper
@author: agungor2
"""




from bs4 import BeautifulSoup
import pandas
from urllib.request import urlopen
b = BeautifulSoup(urlopen("http://www.alexa.com/topsites/category").read())
paragraph = b.find_all('div', {'class':'tableContainer'})
n_p=[]

#Alexa main categories

for p in paragraph:
   print(p.find_all('li'))
   n_p.append(p.find_all('li'))
at=n_p[0]
category=[]
for element in range(len(at)):
    category.append(str(at[element]).split('/')[4].split('"')[0])
    print(category)
    
#Sub Categories for each category
subcategory=[]
sitenumber=[]
for element in range(len(category)):
    kat='http://www.alexa.com/topsites/category/Top/'+str(category[element])
    b = BeautifulSoup(urlopen(kat).read())
    paragraph = b.find_all('div', {'class':'tableContainer'})
    
    n_p=[]
    for p in paragraph:
       print(p.find_all('li'))
       n_p.append(p.find_all('li'))
    at=n_p[0]
#    print(at)
    subcategory.append([])
    sitenumber.append([])
    subcategory[element].append(str(category[element]))
    sitenumber[element].append(str(category[element]))
    for e in range(len(at)):
        c=str(at[e]).split('/')[5].split('"')[0]
        subcategory[element].append(c)
        sitenumber[element].append(c+'-'+str(at[e]).split('(')[1].split(')')[0].replace(',', ''))
#        print(subcategory)
        print(sitenumber)

#Now we need to scrap top websites for each subcategory
#category_sites=[]
category_newsites={}

for i in range(len(category)-1):
#    category_sites.append([])
#    subcategory_sites=[]
#    c_temp=-1
    data=pandas.DataFrame([])
    for j in range(len(subcategory[i])-1):
        l_temp=int(sitenumber[i][j+1].split()[1])
#        Pick the subcategories that have more than 50 websites
        if l_temp >100:
#            c_temp=c_temp+1
            kat='http://www.alexa.com/topsites/category/Top/'+str(category[i])+'/'+str(subcategory[i][j+1])
            b = BeautifulSoup(urlopen(kat).read())
            paragraph = b.find_all('div', {'class':'td DescriptionCell'})
#            subcategory_sites.append([])
            temp=[]
            for p in range (len(paragraph)):
                print(paragraph[p].a.text)
                temp.append(paragraph[p].a.text)
            data[subcategory[i][j+1]] = temp            
#            subcategory_sites[c_temp].append((subcategory[i][j+1],temp))
            print(kat)
    category_newsites[i] = {category[i]: data}
#    category_sites[i].append((category[i],subcategory_sites))
            

#df = pandas.DataFrame(sites)
#df1 = df.transpose()
#df2=df1.iloc[:50][:50]
#df2.to_csv('topsites.csv', sep=',')