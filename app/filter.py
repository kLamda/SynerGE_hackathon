import pandas as pd
import numpy as np
import spacy
from spacy import displacy
from spacy.util import minibatch, compounding
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage
import matplotlib.pyplot as plt
import csv, os


def predict(txt):
  '''PUT THE SPACY WEIGHT FOLDER'''
  
  nlp2 = spacy.load(staticfiles_storage.path("spacy_model"))
  doc2 = nlp2(str(txt))

  if(doc2.cats['SCORE']>0.5):
    return True
  else:
   return False


def classify_csv(path,path2):
  print("Classification Started")
  df=pd.read_csv(path, encoding = "latin")

  df_temp=df
  df_temp.columns =['id', 'txt', 'pr', 'dt','pl']
  df = pd.DataFrame( columns = ['id', 'txt', 'pr', 'dt','pl'])
  
  for i in range(np.array(df_temp).shape[0]):
    if predict(df_temp['txt'][i])==True:
      df=pd.concat([df,df_temp.iloc[[i]]],) 
      #df.drop(df_temp.index[i],inplace=True)
  
  'GIVE THE PATH NAME'
  df.to_csv(path2)
  print("Classification Ended")

time_span=1
import random
from datetime import *


dx = datetime(2016, 5, 24)
def get_id(dt,di=dx):
  d=dt.split('-')
  
  if(len(d)!=3):
    #d=[str(random.randint(1,28)),str(random.randint(1,12)),str(random.randint(2016,2017))]
    return random.randint(0,9)
  
  
     
  dl = datetime(int(d[2]),int( d[1]), int(d[0]))
  #dl=dl-(di-timedelta(days = 7))
  dl=dl-di
  dl=int(dl.days/time_span)
  return dl

def filter_equi(path2,path_equi,dx):
  verbose=False
  thresh=70
  from fuzzywuzzy import fuzz
  df_m=pd.read_csv(path2,index_col=0)
  
  
  lst_s=['surgery']
  lst_sc=['scan','ray','ultrasound','ecg']
  lst_v=['ventilator']
  lst_m=['microscope']
  d1 = dx
  #d2=d1 + timedelta(days = 45)
  lst=[]
  for i in range(int(10/time_span)):
    d1=d1+timedelta(days = time_span)
    lst.append(d1)
  df=pd.DataFrame(lst, columns = ['date']) 
  df['surgery']=0
  df['scaner']=0
  df['ventilator']=0
  df['microscope']=0
  for i in range(np.array(df_m).shape[0]):
    cm=df_m['txt'].iloc[i].split(" ")
    for j in range(len(cm)):
      for sr in lst_s:
        if(fuzz.token_set_ratio(sr,cm[j])>thresh):
          if verbose==True:
            print(fuzz.token_set_ratio(sr,cm[j]),sr,cm[j])
          df['surgery'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['surgery'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
          break
      for scn in lst_sc:
       if(fuzz.token_set_ratio(scn,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(scn,cm[j]),scn,cm[j])
        df['scaner'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['scaner'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break
      for ve in lst_v:
       if(fuzz.token_set_ratio(ve,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(ve,cm[j]),ve,cm[j])
        df['ventilator'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['ventilator'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break
      for mi in lst_m: 
       if(fuzz.token_set_ratio(mi,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(mi,cm[j]),mi,cm[j])
        df['microscope'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['microscope'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break 
  df = df.loc[~((df['surgery'] == 0) & (df['scaner'] == 0) &(df['ventilator'] == 0) &(df['microscope'] == 0))]
  
  df.to_csv(path_equi)

def filter_place(path2,path_state,dx):
  verbose=False
  thresh=85
  from fuzzywuzzy import fuzz
  df_m=pd.read_csv(path2,index_col=0)
  
  
  lst_s=['Delhi']
  lst_sc=['Uttar']
  lst_v=['Maharashtra']
  lst_m=['Rajasthan']
  lst_fi=['Bengal']
  d1 = dx
  #d2=d1 + timedelta(days = 45)
  lst=[]
  for i in range(int(10/time_span)):
    d1=d1+timedelta(days = time_span)
    lst.append(d1)
  df=pd.DataFrame(lst, columns = ['date']) 
  df['Delhi']=0
  df['Uttar Pradesh']=0
  df['Maharashtra']=0
  df['Rajasthan']=0
  df['Bengal']=0
  for i in range(np.array(df_m).shape[0]):
    cm=df_m['pl'].iloc[i].split(" ")
    for j in range(len(cm)):
      for sr in lst_s:
        if(fuzz.token_set_ratio(sr,cm[j])>thresh):
          if verbose==True:
            print(fuzz.token_set_ratio(sr,cm[j]),sr,cm[j])
          df['Delhi'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['Delhi'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
          break
      for scn in lst_sc:
       if(fuzz.token_set_ratio(scn,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(scn,cm[j]),scn,cm[j])
        df['Uttar Pradesh'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['Uttar Pradesh'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break
      for ve in lst_v:
       if(fuzz.token_set_ratio(ve,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(ve,cm[j]),ve,cm[j])
        df['Maharashtra'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['Maharashtra'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break
      for mi in lst_m: 
       if(fuzz.token_set_ratio(mi,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(mi,cm[j]),mi,cm[j])
        df['Rajasthan'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['Rajasthan'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break 
      for mi in lst_fi: 
       if(fuzz.token_set_ratio(mi,cm[j])>thresh): 
        if verbose==True:
            print(fuzz.token_set_ratio(mi,cm[j]),mi,cm[j])
        df['Bengal'].iloc[get_id(df_m['dt'].iloc[i],dx)]=df['Bengal'].iloc[get_id(df_m['dt'].iloc[i],dx)]+1
        break   
  df = df.loc[~((df['Delhi'] == 0) & (df['Uttar Pradesh'] == 0) &(df['Maharashtra'] == 0) &(df['Rajasthan'] == 0)&(df['Bengal'] == 0))] 
  '''give the path of trial state csv'''     
  df.to_csv(path_state)

def get_csv(path1, filt_path, path_equi, path_state, keep_backup = False):
  print("Filtration started")
  dff=pd.read_csv(path1, encoding = "latin")
  dff.columns =['id', 'txt', 'pr', 'dt','pl']
  dx=None
  for i in range(np.array(dff).shape[0]):
    dt=dff['dt'][np.array(dff).shape[0]-1-i]
    d=dt.split('-')
    if(len(d)==3):
      dx= datetime(int(d[2]),int( d[1]), int(d[0]))
      break
      
  if dx==None:
    dx= datetime(2020,12,28)

  # '''give the path of filtered csv'''
  # # filt_path='filt.csv'
  # '''give the path of filtered equi_csv'''
  # path_equi='equi.csv'
  # '''give thw path of filtered state_csv'''
  # path_state='state.csv'
  
  classify_csv(path1,filt_path)
  filter_equi(filt_path,path_equi,dx)
  filter_place(filt_path,path_state,dx)
  print("Filtration Ended")
  # if not keep_backup:
  #     os.remove(path1)

def update_data(filt_equi_path, filt_state_path, equi_path, state_path, no_days, keep_backup = False):
    df = pd.read_csv(equi_path)
    df = df.drop(['Unnamed: 0'], axis=1)
    equi_list = df.values.tolist()
    df2 = pd.read_csv(state_path)
    df2 = df2.drop(['Unnamed: 0'], axis=1)
    state_list = df2.values.tolist()
    with open(filt_state_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(no_days):
            writer.writerow(state_list[i])
    with open(filt_equi_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(no_days):
            writer.writerow(equi_list[i])
    # if not keep_backup:
    #     os.remove(equi_path)
    #     os.remove(state_path)