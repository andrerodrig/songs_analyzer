#libraries
from cProfile import label
from ctypes import alignment
from logging import PlaceHolder
import streamlit as st
import spotipy
import pandas as pd
import numpy as np
import time
from spotipy.oauth2 import SpotifyClientCredentials

#page config
st.set_page_config(
     page_title="Song Recomendator",
     page_icon="🎧",
     layout="wide",
     menu_items={
         'Get Help': 'https://github.com/andrerodrig/songs_analyzer',
         'Report a bug': "https://github.com/andrerodrig/songs_analyzer",
         'About': "# Song Recomendator app!"
     }
 )

#data structures
options = []
album_art = []
uri = []

#credentials
client_ID=''
client_SECRET=''

#credentials object
client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#page title
st.title("🎧 Song Recomendator 🎧")

try:
    #receives data from user and searches on spotify API
    user_song = st.text_input(label='Busca',help='Digite sua música e tecle Enter')
    data = sp.search(q=user_song, type="track", limit=5)
except:
    st.warning('Você digitou algo? 🤔 ')

try:
    with st.spinner('Processando... 😎 '):
        time.sleep(1)
        
        for x in range(5):
            options.append([
                data['tracks']['items'][x]['artists'][0]['name'],
                data['tracks']['items'][x]['name']
            ])
            album_art.append([
                data['tracks']['items'][x]['album']['images'][2]['url']
            ])
            uri.append([
                data['tracks']['items'][x]['uri']
            ])



        df = pd.DataFrame(options)
        df = df.rename(columns={0:'artista',1:'título'})

        select = df['artista']+' - '+df['título']

        st.success('Agora selecione sua música 👇')
        option = st.radio(
            "",(select)
            )
        st.write(option)
except:
    pass
