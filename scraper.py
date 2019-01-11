import urllib.request as url 
from bs4 import BeautifulSoup
import pandas as pd 

urllist = ['https://summerofcode.withgoogle.com/archive/2018/organizations','https://summerofcode.withgoogle.com/archive/2017/organizations','https://summerofcode.withgoogle.com/archive/2016/organizations']

df = pd.DataFrame(columns = ['Name','Field','Year','Link'])

for i in urllist:
    year = i.split('/')[-2]
    page = url.urlopen(i)
    soup  = BeautifulSoup(page,features="html.parser")
    containers = soup.findAll('li',attrs={'class': 'organization-card__container'})
    for j in containers:
        temp= j.get_text().strip().split('\n')
        link = i+j.a['href']
        df = df.append({'Name':temp[0],'Field':temp[1],'Year':year,'Link':link},ignore_index = True)
print(df)

