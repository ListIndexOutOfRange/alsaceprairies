import os
from google.cloud import firestore

ROOTDIR  = "/home/almotasim/Documents/NON_DL_DEV/App/FARMERS/alsaceprairies/pages/database/"
KEY_NAME = "firestore_key.json"

def connect_and_dl_db():
    db = firestore.Client.from_service_account_json(os.path.join(ROOTDIR, KEY_NAME))
    return db.collection("travaux")


def format_line(document):
    line = {}
    line['N° parcelle'] = document['caracteristiques']['numero']
    line['Types de Travaux'] = ""
    for type_travaux in ['mecaniques', 'manuels', 'resemis']:
        if document[type_travaux]:
            line['Types de Travaux'] += (type_travaux + ", ")
    line['Types de Travaux'] = line['Types de Travaux'][:-2]
    line['Types de Travaux'] = [line['Types de Travaux']]
    line['Date'] = document['date']
    return line


def format_data_to_table(data):
    lines = []
    for id in range(len(data.get())):
        lines.append(format_line(data.document(str(id)).get().to_dict()))
    return lines


def format_data_to_db(caracteristiques, mecaniques, manuels, resemis, date):
    #TODO
    return