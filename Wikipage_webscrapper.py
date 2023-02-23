from  bs4 import BeautifulSoup
import requests
from datetime import date
import pandas as pd

#Url of webpage
wikiurl= "https://en.wikipedia.org/wiki/List_of_best-selling_Nintendo_Switch_video_games"
response=requests.get(wikiurl)

soup = BeautifulSoup(response.text, 'html.parser')

#finds html tag table with class attribute wikitable
table=soup.find('table',{'class':"wikitable"})

#convert the variable table string into list
df=pd.read_html(str(table))

# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())
# convert to CSV
df.to_csv('nintendo.csv')