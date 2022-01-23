import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import recommender, upload, about

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Recomendador", recommender.app)
app.add_page("Envie sua playlist", upload.app)
app.add_page("Sobre", about.app)

# The main app
app.run()