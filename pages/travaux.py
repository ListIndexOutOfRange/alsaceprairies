import streamlit as st
from .database import connect_and_dl_db, format_data_to_table

NUMBER_INPUT_KWARGS = {"min_value": 0, "max_value": 1000, "value": 0}

def display(data, id):
    doc = data.document(str(id)).get().to_dict()
    st.subheader("Caractéristiques")
    left, mid, right = st.beta_columns(3)
    left.write(f"Numero de parcelle: {doc['caracteristiques']['numero']}")
    mid.write(f"Surface: {doc['caracteristiques']['surface']} ha")
    right.write(f"Pente: {doc['caracteristiques']['pente']}")
    st.write(f"Date: {doc['date']}")
    st.write("Work in progress")


def infos(data):
    nb_travaux = len(data.get())
    with st.beta_expander("Afficher plus d'informations sur un travail en cours"):
        st.write("Pour afficher plus d'information sur un travail en cours, \
            veuillez entrer son numéro (le numéro dans la colonne la plus à gauche) \
            plus cliquer sur le bouton ci-dessous.")
        left, right = st.beta_columns(2)
        id = left.number_input("Numéro du travail", **NUMBER_INPUT_KWARGS)
        lines_skip = 2
        for _ in range(lines_skip):
            right.write('')
        more_infos = right.button("Afficher plus d'informations")
        if more_infos:
            if id >= nb_travaux:
                st.warning("Désolé, vous n'avez pas entré un numéro de travail en cours.")
            else:
                display(data, id) 


def content():
    st.title("Travaux en cours")
    data = connect_and_dl_db()
    st.table(*format_data_to_table(data))
    infos(data)