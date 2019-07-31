import pandas as pd
from faker import Faker
import random

def create_rows(num=1):
    fake=Faker()
    #lookup data
    race_list = ['Caucasoid Aryan(Western and Northern Europe)'
        , 'Slavic(Eastern Europe and Russia)'
        ,
                 'Western Negroid(Western Africa and most African Americans as they were taken to the United States from Western Africa)'
        , 'Sub Aryan(Spain, Italy, Greek)'
        , 'Middle Eastern Caucasoid (Saudi Arabia/ White part of Egypt/ Middle East)'
        , 'Eastern Negroid (Somalia/Ethiopia/Sudan/Chad)'
        , 'Mongolese (ancestor to many of the current Asians)'
        , 'Indo-Aryan(much of northern India, Pakistan, Iran)'
        , 'Dravidans (South India/ Sri Lanka)'
        , 'Australoid(Australian natives, indonesia)'
        , 'American Natives (Cherokee/ Al paca tribes)'
        , 'Jewish (Azekhazani Jews)'
        , 'Mixes of races(Brazil = mix between native Americans, spanish and black)']
    #dataset schema
    output = [{"name": fake.name(),
               "address": fake.address(),
               "email": fake.email(),
               "bs": fake.bs(),
               "city": fake.city(),
               "state": fake.state(),
               "date_time": fake.date_time(),
               "paragraph": fake.paragraph(),
               "conrad": fake.catch_phrase(),
               "race": race_list[random.randrange(len(race_list)-1)],
               "latitude":fake.latitude(),
               "longitude":fake.longitude()
              } for _ in range(num)]
    return output
if __name__=='__main__':
    #dataset columns
    cols=['name','address','email','bs', 'city','state','date_time','paragraph','conrad','race']
    df=pd.DataFrame(create_rows(100), columns=cols)
    # dataset name
    df.to_csv('sample_data.csv',index=None, header=True)
    print("Done")
