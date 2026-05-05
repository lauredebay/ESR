# l'objectif de ce TP est vd'analyser la base de données E+C_
# d'analyse ACV (Analyse du Cycle de Vie) des produits de construction
# grace à l'application streamlit pour visualiser les données et faire des analyses

#Instruction pour éxécuter l'application :
# conda activate ESTPdata
# streamlit run TP_AVC.py

# rappel pour déploiement de l'application sur streamlit cloud :
# uploader dans un repo github 
# creer l'app dans streamlit 

#STEP 1 : importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time 

#STEP 2 : présentation de l'application
st.title("Analyse ACV - E+C-")
st.write("Bienvenue dans cette application d'analyse ACV pour les produits de construction.")

# STEP 3 : chargement d'un fichier
uploaded_file = st.file_uploader("Téléversez un fichier Excel (.xlsx)", type="xlsx")
if uploaded_file is not None:
    st.write("Fichier chargé avec succès !")
    try:
        df = pd.read_excel(uploaded_file, sheet_name='batiments', header=[0, 1])  # lecture de l'onglet 'batiments' avec les deux premières lignes comme en-têtes
        df.columns = df.columns.droplevel(0)
      # lecture de l'onglet 'batiments'
    except ValueError:
        st.error("La feuille 'batiments' est introuvable dans le fichier Excel.")
        df = None
    if df is not None:

        st.write("Aperçu des 5 premières lignes du jeu de données :")
        st.dataframe(df.head(5))  # affichage des 5 premières lignes du dataframe dans streamlit

        # STEP 4 : tracé scatter plot avec Plotly de la colonne 'eges' (émissions de gaz à effet de serre)
        st.subheader("Visualisation de la colonne 'eges' (émissions de gaz à effet de serre)")
        if 'eges' in df.columns:
            x_candidates = [col for col in df.columns if col != 'eges']
            if x_candidates:
                x_col = st.selectbox("Sélectionnez une colonne pour l'axe des x", x_candidates)
                df_plot = df[[x_col, 'eges']].copy()  # sélection de la colonne x et de 'eges', suppression des lignes avec NaN
                df_plot = df_plot.dropna(subset=[x_col, 'eges'])
                fig = px.scatter(df_plot, x=x_col, y='eges', title="Nuage de points des émissions de gaz à effet de serre (eges)")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Aucune colonne disponible pour l'axe des x.")
        else:
            st.warning("La colonne 'eges' (émissions de gaz à effet de serre) est introuvable dans l'onglet 'batiments'. Vérifiez le nom ou la présence de la colonne.")

