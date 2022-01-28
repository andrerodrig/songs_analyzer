from pathlib import Path
from joblib import dump, load
from ast import keyword
import streamlit as st
import pandas as pd
from argostranslate import package, translate
from songs_analyzer.data import spotify
import numpy as np


# tradutor
package.install_from_path('models/translate-pt_en-1_0.argosmodel')
installed_languages = translate.get_installed_languages()
pt2en = installed_languages[1].get_translation(to=installed_languages[0])

transformer = load("models/transformer.model")
neigh = load("models/neigh.model")
df = pd.read_csv(Path("data/processed/data.csv"))
df = df.assign(
    name=df.name.apply(lambda x: np.str_(x)),
    artist=df.artist.apply(lambda x: np.str_(x)),
    genrers=df.genrers.apply(lambda x: np.str_(x)),
).query("name.str.len() > 2 and artist.str.len() > 1 and genrers.str.len() > 1")

def app():
    st.title("Recomendador") 
    keyword = st.text_input(label='Busca', help='Digite sua música e tecle Enter')
    if keyword:
        songs = spotify.get_songs(keyword)
        song_info = [
            {
                "name": song["name"],
                "uri": song["uri"],
                "artist": song["album"]["artists"][0]["name"]
            }
            for song in songs["tracks"]["items"]
        ]
        options = [f"{song['artist']} | {song['name']}" for song in song_info]
        selected_song = st.radio("Selecione a música escolhida.", options=options)
        if selected_song:
            song = song_info[options.index(selected_song)]
            with st.spinner('Processando...'):
                st.subheader("Recomendações")
                uri = song["uri"]
                track = spotify.get_track_geatures(spotify.get_track_by_uri(uri))
                track["genrers"] = ' '.join(track["genrers"])
                track["artist"] = str(track["artist"]).lower()
                track["name"] = pt2en.translate(str(track["name"]).lower())
                x_test = pd.DataFrame(track, index=[1])
                
                songs = neigh.kneighbors(transformer.transform(x_test), return_distance=False)
                rec = []
                for song_uri in df.iloc[songs[0]].uri:
                    if song_uri != uri:
                        song = spotify.get_track_geatures(spotify.get_track_by_uri(song_uri))
                        url = f'https://open.spotify.com/track/{song["uri"].split(":")[-1]}'
                        rec.append(f" - [{song['artist']} | {song['name']}]({url})")
                st.markdown('\n'.join(rec))
    else:
        st.warning("Por favor, insira uma palavra chave.")