#libraries
import streamlit as st
import spotipy
import pandas as pd
import numpy as np
import json
from spotipy.oauth2 import SpotifyClientCredentials

#data structures
song = {
    'track_artist': [],
    'track_name': [],
    'track_uri':[]
}


#credentials
client_ID=''
client_SECRET=''

#credentials object
client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#page title
st.title("Song Recomendator")

#receives data from user and searches on spotify API
user_song = st.text_input("Digite o título da música")
data = sp.search(q=user_song, type="track", limit=5)


for x in range(5):
    song['track_artist'].append(data['tracks']['items'][x]['artists'][0]['name'])
    song['track_name'].append(data['tracks']['items'][x]['name'])
    song['track_uri'].append(data['tracks']['items'][x]['uri'])


option = st.radio(
     "Encontramos as seguintes músicas",('','','','','')
     )

#writes what was found on spotify API
st.write(song)