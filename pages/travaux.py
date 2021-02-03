import streamlit as st

NUMBER_INPUT_KWARGS = {"min_value": 0, "max_value": 1000, "value": 0}

#################################################################
#                   FOR DEVELOPMENT ONLY
#################################################################
import pickle

def load_data():
    with open('sample_data.pickle', 'rb') as handle:
        return pickle.load(handle)


def display_full_data(data, id):
    st.write(data)


def infos(data):
    nb_travaux = len(data)
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
                display_full_data(data, id) 


def format_data(data):
    line = {}
    line['Numero'] = data['caracteristiques']['numero']
    line['Types de Travaux'] = ""
    for type_travaux in ['mecaniques', 'manuels', 'resemis']:
        if data[type_travaux]:
            line['Types de Travaux'] += (type_travaux + ", ")
    line['Types de Travaux'] = line['Types de Travaux'][:-2]
    line['Types de Travaux'] = [line['Types de Travaux']]
    line['Date'] = data['data'] 
    return line


def content():
    st.title("Travaux en cours")
    data = load_data()
    line = format_data(data)
    st.table(line)
    infos(data)