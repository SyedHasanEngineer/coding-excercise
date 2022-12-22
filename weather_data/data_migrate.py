import pandas as pd
import datetime
from sqlalchemy import create_engine
from django.conf import settings
import pymysql
import os


def weather_data_dump(path):
    file_data = []
    columns=['date','min_temp','max_temp','precipitation']
    data = open(path).readlines()
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    return file_data


def yield_data_dump():
    path = r"D:\code-challenge-template\yld_data\US_corn_grain_yield.txt"
    columns=['date','corn_gain']
    data = open(path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    user = "root"
    password = "Admin21$"
    database_name = "weather"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weatheryield", con=engine)


def weather_stats(path):
    columns=['date','min_temp','max_temp','precipitation']
    data = open(path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    return dataframe[(dataframe['precipitation']!='-9999') & 
                     (dataframe['max_temp']!='-9999') & 
                     (dataframe['min_temp']!="-9999")]


def calculate_stats(path):
    result = []
    columns=['date','min_temp','max_temp','precipitation']
    df = weather_stats(path)
    df['date'] = list(map(lambda x:datetime.datetime.fromtimestamp(float(x)),df['date']))
    df['year'] = list(map(lambda x:df['date'].dt.year,df.index))
    df['max_temp']=list(map(float,df['max_temp'].values))
    df['min_temp']=list(map(float,df['min_temp'].values))
    df['precipitation']=list(map(float,df['precipitation'].values))
    df.year = df.year.apply(str)
    mean = df.groupby('year').mean()
    total = df.groupby('year').sum()
    maximutemp_mean  = mean['max_temp']
    minimutemp_mean = mean['min_temp']
    total_precipitation = total['precipitation']

    dataframe = pd.DataFrame()

    dataframe['avg_max_temp']= list(map(float,maximutemp_mean.values))
    dataframe['avg_min_temp']=list(map(float,minimutemp_mean.values))
    dataframe['avg_total_prcecitipation']=list(map(float,total_precipitation.values))

    dataframe.index.names = ['id']
    user = "root"
    password = "Admin21$"
    database_name = "weather"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weather_status", con=engine)


def read_data(path):
    file_data=weather_data_dump(path)
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    user = "root"
    password = "Admin21$"
    database_name = "weather"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weather", con=engine)


if __name__ == "__main__":
    path = r"D:\code-challenge-template\wx_data\USC00110072.txt"
    read_data(path)
    yield_data_dump()
    calculate_stats(path)


