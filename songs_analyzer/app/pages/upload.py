from pathlib import Path
import json

import streamlit as st
from songs_analyzer.data import spotify

def app():
    st.title("Envie sua playlist")
    url = st.text_input(
        "Playlist url",
        help="Spotify playlist URL, for example: https://open.spotify.com/playlist/20BPPt8TYRA4GrNVKOQH5Y"
    )
    enviar = st.button("Enviar playlist")
    if enviar:
        uri = url.split("/")[-1].split("?")[0]
        playlist_path = Path(f"data/raw/playlists/new/{uri.split(':')[-1]}.json")
        old_playlist_path = Path(f"data/raw/playlists/new/{uri.split(':')[-1]}.json")
        if playlist_path.exists() or old_playlist_path.exists():
            st.info("Já temos essa Playlist em nosso banco de dados, poderia enviar outra?")
        else:
            try:
                track_list = spotify.get_tracks_from_playlist(uri)
                track_feature_list = []
                st.info("Inserindo músicas, por favor, aguarde.")
                my_bar = st.progress(0)
                for i, track in enumerate(track_list):
                    try:
                        track_feature_list.append(spotify.get_track_geatures(track))
                    except:
                        st.warning("Algum erro inesperado ocorreu. Tente enviar outra URL.")
                    my_bar.progress((i+1) / len(track_list))
                with open(playlist_path, 'w+') as file:
                    json.dump(track_feature_list, file)
                st.balloons()
                st.success('Muito obrigado por contribuir com o nosso projeto!')
            except Exception as e:
                print(e)
                st.warning("Essa não é uma URL válida.")
    else:
        st.warning("Por favor, insira uma URL.")