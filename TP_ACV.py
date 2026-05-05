# l'objectif de ce TP est vd'analyser la base de données E+C_
# d'analyse ACV (Analyse du Cycle de Vie) des produits de construction
# grace à l'application streamlit pour visualiser les données et faire des analyses
 
#Instruction pour éxécuter l'application :
# conda activate ESTP-TNC
# streamlit run TP_ACV.py
 
# rappel pour deployer sur streamlit cloud :
# 1. créer un compte sur https://streamlit.io/
# 2. créer un nouveau projet et connecter votre dépôt GitHub

#STEP 1 : importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import numpy as np
import time 

# plotly is optional; fallback to Streamlit built-in charts if unavailable
try:
    import plotly.express as px
    plotly_available = True
except ImportError:
    plotly_available = False
 
#STEP 2 : présentation de l'application
st.title("Analyse ACV - E+C-")
st.write("Bienvenue dans cette application d'analyse ACV pour les produits de construction.")
 
 #STEP 3 : chargement de la base de données
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=['xlsx', 'xls'])
df = None
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Aperçu des 5 premières lignes :")
    st.dataframe(df.head())

#STEP 4 : visualisation avec plotly scatter plot
if df is not None:
    y_col = st.selectbox("Choisissez la colonne pour l'axe Y", df.columns)
    if plotly_available:
        fig = px.scatter(df, y=y_col)
        st.plotly_chart(fig)
    else:
        st.warning("Plotly n'est pas installé. Affichage avec un graphique Streamlit par défaut.")
        st.line_chart(df[[y_col]])