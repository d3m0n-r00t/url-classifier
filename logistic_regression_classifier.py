import pandas as pd 
import numpy as np
import random 
import io
import requests
import time
import pickle
from sklearn.preprocessing import LabelEncoder 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from urllib.parse import urlparse

#Setting up data. Setting the variables and targets. And encoding
def setting_data():
    data_file='data.csv'
    data_csv=pd.read_csv(data_file)
    data_frame=pd.DataFrame(data_csv)
    data=np.array(data_frame)
    random.shuffle(data)
    y=[d[1]for d in data]
    x=[d[0]for d in data]
    return x,y

def tokeniser(input):
  basic_token=urlparse(input)
  tokens=[]
  domain=str(basic_token.netloc)
  path=str(basic_token.path)
  method=str(basic_token.scheme)
  tokens.extend([domain,path,method])
  tokens=list(set(tokens))
  return tokens

def encoder(x,y):
    lb_make=LabelEncoder()
    Y=lb_make.fit_transform(y)
    vectorizer=TfidfVectorizer(tokenizer=tokeniser)
    X=vectorizer.fit_transform(x)
    return X,y

#Creating a model with data.
def modeling(X,Y):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model=LogisticRegression()  
    model.fit(X_train,Y_train)
    return model,X_test,Y_test

if __name__ == "__main__":
    x,y=setting_data()
    X,Y=encoder(x,y)
    model,X_test,Y_test=modeling(X,Y)
    #Saving the model
    print('Saving model to the disk.')
    timestr=time.strftime("%Y%m%d-%H%M%S")
    filename='model'+timestr+'.sav'
    pickle.dump(model,open(filename,'wb'))
    print('Model saved successfully')
    #Loading model
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(X_test, Y_test)
    print('Model loaded successfully. Printing test scores: ',result)