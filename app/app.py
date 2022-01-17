#libraries
import streamlit as st
import spotipy
import pandas as pd
import numpy as np
import json
from spotipy.oauth2 import SpotifyClientCredentials

#data structures
song = {
    0:[],
    1:[],
    2:[],
    3:[],
    4:[]
}
buttons = {}

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
    song[x].append({
        data['tracks']['items'][x]['artists'][0]['name'],
        data['tracks']['items'][x]['name'],
        data['tracks']['items'][x]['uri']
        })
    
    


option = st.radio(
     "Encontramos as seguintes músicas",(song[0],song[1],song[2],song[3],song[4])
     )

#writes what was found on spotify API
result = st.button('Recomendar')