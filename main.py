import requests
import hashlib
import datetime
import time
import models
import pandas as pd
from IPython.display import display
from models import Base
from db import SessionLocal, engine


def retrieve_data():
    response_api = requests.get('https://restcountries.com/v3.1/all')
    countries = response_api.json()
    df = pd.DataFrame(columns = ['region', 'city_name', 'language', 'time'])
    i = 1
    
    for country in countries:
        time_st = datetime.datetime.now()
        capital = country['capital'][0] if 'capital' in country.keys() else None
        language_hash = hashlib.sha1(list(country['languages'].values())[0].encode('utf-8')).digest() if 'languages' in country.keys() else None
        time_total = datetime.datetime.now() - time_st
        time_ex = time_total.microseconds
        df.loc[i] = (country['region'], capital , str(language_hash), time_ex)
        i += 1
    df.to_sql('cities', engine, if_exists='replace')
    total = df['time'].sum()
    minimum = df['time'].min()
    maximum = df['time'].max()
    avg = df['time'].mean()

    df_final = pd.DataFrame(columns=['total', 'promedio', 'minimo', 'maximo'])
    df_final.loc[0] = (total, avg, minimum, maximum)
    df.to_sql('times', engine, if_exists='replace')


if __name__ == "__main__":
    retrieve_data()