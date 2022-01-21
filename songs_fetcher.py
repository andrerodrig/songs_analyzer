#libraries
import spotipy
import pandas as pd
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

#credentials
client_ID='b9d578d1b408480c9ad1ea3790a298a2'
client_SECRET='c31a76b2807d4503aefff08310af74b9'

#credentials object
client_credentials_manager = SpotifyClientCredentials(client_id=client_ID, client_secret=client_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#read playlists csv
df = pd.read_csv('data/raw/playlists_uri_name.csv')
print
uris = df['uri'].array
for y in uris:
    #track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(uris[y])["items"]]
    track_uris = sp.playlist_tracks(y)['items']
print(track_uris)