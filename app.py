import streamlit as st
import pandas as pd

#chargement du dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)






# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue sur le site web de YANIS")

# Liste des arrondissements disponibles
boroughs = df["pickup_borough"].dropna().unique()
boroughs.sort()


# menu déroulant
selection = st.selectbox("Indiquez votre arrondissement de récupération", boroughs) 

# affichage du choix
st.write(f"Tu as choisi : {selection}")

# affichage de l'image associée
image_path = f"images/{selection.lower().replace(' ', '_')}.jpg"

st.image (image_path, caption=selection)