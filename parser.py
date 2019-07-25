import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading


URL_PATH = "https://www.alexa.com/siteinfo/{}"

def alexa_ranking_thread(url, index):
    response = requests.get(URL_PATH.format(url)).content
<<<<<<< HEAD
    bs4 = BeautifulSoup(response, 'html.parser')
=======
    bs4 = BeautifulSoup(response.content, 'html.parser')
>>>>>>> e85345610e065706eebcb9ef19d13e4ad4c79a7b
    alex_rank = bs4.find("div",{"class":"rankmini-rank"}).get_text().strip().strip("#")
    data['Alexa Ranking'][index] = alex_rank

data = pd.read_csv('data.csv').rename(columns={'Unnamed: 2':'Alexa Ranking'})
<<<<<<< HEAD
data = data[['url','Alexa Ranking','label']]

=======
data = data[['url','Alexa Ranking']]
print(data.head())
>>>>>>> e85345610e065706eebcb9ef19d13e4ad4c79a7b

for i in range(data.shape[0]):
    url = data['url'][i]
    try:
       thread = threading.Thread(target = alexa_ranking_thread,args=(data['url'][i],i,))
       thread.start()
<<<<<<< HEAD
       print(i)
       data.to_csv('modified.csv')
    except KeyboardInterrupt:
      break
=======
       data.to_csv('modified.csv')
    except KeyboardInterrupt:
       pass
>>>>>>> e85345610e065706eebcb9ef19d13e4ad4c79a7b
