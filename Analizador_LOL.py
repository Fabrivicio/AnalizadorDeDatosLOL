#!/usr/bin/env python
# coding: utf-8

# In[47]:


import requests 
from time import sleep
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# In[48]:


api_key= 'API CODE'                     #Importamos el api de Riot Games (Caduca cada 24hrs)


# In[111]:


servers= {
    'br1' : 'br1',
    'eun1' : 'eun1',
    'euw1' : 'euw1',
    'jp1' : 'jp1',
    'kr' : 'kr',
    'la1' : 'la1',                                                      #Agregamos todos los servidores de los juegos
    'la2' : 'la2',
    'na1' : 'na1',
    'oc1' : 'oc1',
    'ru' : 'ru',
    'tr1' : 'tr1',
    
    
    
    
}


# In[112]:


summ_name = 'jomi404'
user_per_server = {}

for server in servers:
    endpoint = f'https://{server}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summ_name}?api_key={api_key}'        #Agregamos el nombre de usuario del jugador que queremos 
                                                                                                                            #analizar
    
    res = requests.get(endpoint).json()
    if res.get('status', None):
        print (f'No se encuentra el usuario en {server}: {res}')
    else:
        print (f'Se encontro al usuario en {server}') 
        user_per_server[server] = res
    sleep (1)
  


# In[113]:


user_per_server                                                                                                           #muestra el id del jugador


# In[124]:


servers = ['la2']

for server in servers:
    summ_id = user_per_server[server]['id']
    endpoint = f'https://{server}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summ_id}?api_key={api_key}'              
   
    res = requests.get(endpoint).json()
    print (res)


# In[ ]:





# In[130]:


server = 'la2'
summ_id = user_per_server[server]['id']
endpoint = f'https://{server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summ_id}/top?api_key={api_key}'

res = requests.get(endpoint).json()


# In[131]:


res


# In[134]:


puuid = user_per_server['la2']['puuid']
match_server='americas.api.riotgames.com'
endpoint = f'https://{match_server}/lol/match/v5/matches/by-puuid/{puuid}/ids?api_key={api_key}&start=0&count=20'

res = requests.get(endpoint).json()


# In[128]:


res


# In[135]:


match_id = res[0]
endpoint = f'https://{match_server}/lol/match/v5/matches/{match_id}?api_key={api_key}'
res = requests.get(endpoint).json()

res


# In[137]:


res.keys()


# In[138]:


res['metadata']


# In[139]:


match_stats = ''
for player in res['info']['participants']:
    if player ['puuid'] == user_per_server[server]['puuid']:
        match_stats = player


# In[140]:


match_stats


# In[141]:


stats = [
    'item0',
    'item1',
    'item2',
    'item3',
    'item4',
    'item5',
    'item6',
    'kills',
    'lane',
    'teamPosition',
    'totalMinionsKilled',
    'win',
    
]

for stat in stats:
    print(f'{stat}:{match_stats[stat]}')


# In[144]:


version_lst = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()
res = requests.get(f'https://ddragon.leagueoflegends.com/cdn/{version_lst[0]}/data/en_US/item.json').json()
res


# In[145]:


items= [
    'item0',
    'item1',
    'item2',
    'item3',
    'item4',
    'item5',
    'item6',
    
]


for item_id in items:
    print (res['data'][f'{match_stats[item_id]}'])
    print()


# In[ ]:




