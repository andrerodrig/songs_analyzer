from pathlib import Path
import json

import toml
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

credentials = toml.load(Path(__file__).parents[2] / Path("secret.toml"))

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(**credentials))


def get_track_by_uri(uri):
    return sp.track(uri)
    
def get_tracks_from_playlist(uri):
    results = sp.playlist_tracks(uri, limit=100)
    tracks = [x["track"] for x in results["items"]]
    while results['next']:
        results = sp.next(results)
        tracks.extend([x["track"] for x in results["items"]])
    return tracks

def get_track_geatures(track):
    track_features = sp.audio_features(track["uri"])[0]
    artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
    return {
        'uri': track["uri"],
        'name': track["name"],
        'artist': artist["name"],
        'genrers': artist["genres"],
        'popularity': track["popularity"],
        'danceability': track_features['danceability'],
        'energy': track_features['energy'],
        'key': track_features['key'],
        'loudness': track_features['loudness'],
        'mode': track_features['mode'],
        'speechiness': track_features['speechiness'],
        'acousticness': track_features['acousticness'],
        'instrumentalness': track_features['instrumentalness'],
        'liveness': track_features['liveness'],
        'valence': track_features['valence'],
        'tempo': track_features['tempo'],
        'duration_ms': track_features['duration_ms'],
        'time_signature': track_features['time_signature'],
    }

def get_songs(keyword):
    return sp.search(q=keyword, type="track", limit=5)