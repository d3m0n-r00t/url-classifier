import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading


URL_PATH = "https://www.alexa.com/siteinfo/{}"

def alexa_ranking_thread(url, index):
    response = requests.get(URL_PATH.format(url)).content
    bs4 = BeautifulSoup(response, 'html.parser')
    alex_rank = bs4.find("div",{"class":"rankmini-rank"}).get_text().strip().strip("#")
    data['Alexa Ranking'][index] = alex_rank

data = pd.read_csv('data.csv').rename(columns={'Unnamed: 2':'Alexa Ranking'})
data = data[['url','Alexa Ranking']]
print(data.head())


for i in range(data.shape[0]):
    url = data['url'][i]
    try:
       thread = threading.Thread(target = alexa_ranking_thread,args=(data['url'][i],i,))
       thread.start()
       data.to_csv('modified.csv')
    except KeyboardInterrupt:
       pass
