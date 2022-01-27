from ast import keyword
import streamlit as st
from songs_analyzer.data import spotify



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
    else:
        st.warning("Por favor, insira uma palavra chave.")