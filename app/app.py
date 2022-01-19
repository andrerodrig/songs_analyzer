#libraries
import streamlit as st
import spotipy
import pandas as pd
import numpy as np
import json
from spotipy.oauth2 import SpotifyClientCredentials

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
st.title("Song Recomendator")

try:
    #receives data from user and searches on spotify API
    user_song = st.text_input("Digite o título da música")
    data = sp.search(q=user_song, type="track", limit=5)
except:
    pass

try:
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
except:
    pass


option = st.radio(
     "Encontramos as seguintes músicas",(options)
     )
#st.write(options)
#writes what was found on spotify API
result = st.button('Recomendar')
