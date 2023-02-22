from  bs4 import BeautifulSoup
import requests
from datetime import date
import pandas as pd

wikiurl= "https://en.wikipedia.org/wiki/List_of_best-selling_Nintendo_Switch_video_games"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)

soup = BeautifulSoup(response.text, 'html.parser')
table=soup.find('table',{'class':"wikitable"})
table

df=pd.read_html(str(table))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())

df.to_csv('nintendo.csv')