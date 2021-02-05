import streamlit as st
from .liste_materiel import liste_materiel
from .database import format_data_to_db
from time import sleep # TEMPORARY ONLY



NUMBER_INPUT_KWARGS = {"min_value": 0, "max_value": 1000, "value": 0}


def get_caracteristiques():
    numero  = st.number_input("N° ilot PAC", **NUMBER_INPUT_KWARGS)
    surface = st.number_input("Surface(ha)", **NUMBER_INPUT_KWARGS)
    pente   = st.select_slider("Pente", options=["faible", "moyenne", "élevée"])
    return {'numero': numero, 'surface': surface, 'pente': pente}


def travail_mecanique():
    with st.beta_expander("Travail Mécanique"):
        st.subheader("Passage(s) sur la parcelle:")
        st.write("A chaque passage correspond un ensemble de matériel utilisés en combiné et une durée.")
        nb_passages = st.number_input("Nombre de passages", **NUMBER_INPUT_KWARGS, key="nb_passages_mecaniques")
        passages = []
        for i in range(nb_passages):
            st.markdown("____")
            st.write(f"Passage n°{i+1}")
            passages[i] = {}
            passages[i]["materiel"] = st.multiselect("Matériel", liste_materiel, key=i)
            passages[i]["duree"] = st.number_input("Durée (h)", **NUMBER_INPUT_KWARGS, key=i)
    return passages


def travail_manuel():
    with st.beta_expander("Travail Manuel"):
        st.subheader("Passage(s) sur la parcelle:")
        st.write("A chaque passage correspond un matériel et une durée.")
        nb_passages = st.number_input("Nombre de passages", **NUMBER_INPUT_KWARGS, key="nb_passages_manuels")
        passages = []
        for i in range(nb_passages):
            st.markdown("____")
            st.write(f"Passage n°{i+1}")
            passages[i] = {}
            passages[i]["materiel"] = st.text_input("Matériel utilisé", key=i)
            passages[i]["duree"] = st.number_input("Durée (h)", **NUMBER_INPUT_KWARGS, key=i)
    return passages


def travail_resemis():
    with st.beta_expander("Resemis"):
        st.subheader("Espèce(s) implantée(s):")
        st.write("A chaque espèce implantée est associée un nom, une quantité et un prix.")
        nb_especes = st.number_input("Nombre d'espèces implantées", **NUMBER_INPUT_KWARGS)
        especes = []
        for i in range(nb_especes):
            st.markdown("____")
            st.write(f"Espèce n°{i+1}")
            especes[i] = {}
            especes[i]["nom"] = st.text_input("Nom", key=i)
            especes[i]["quantite"] = st.number_input("Quantitée utilisée (kg/ha)", **NUMBER_INPUT_KWARGS, key=i)
            especes[i]["prix"] = st.number_input("Prix d'achat (€/kg)", **NUMBER_INPUT_KWARGS, key=i)
    return especes


def validation(caracteristiques, mecaniques, manuels, resemis, date):
    with st.spinner("Ajout du travail en cours..."):
        format_data_to_db(caracteristiques, mecaniques, manuels, resemis, date)
        sleep(5)
    st.success("Travail enregistré !")


def content():
    st.title("Ajouter un travail")
    caracteristiques = get_caracteristiques()
    mecaniques = travail_mecanique()
    manuels = travail_manuel()
    resemis = travail_resemis()
    date = st.date_input("Date")
    st.markdown("____")
    if st.button("Valider"):
        validation(caracteristiques, mecaniques, manuels, resemis, date)
