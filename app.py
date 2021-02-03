import pages.travaux as travaux
import pages.ajout_travail as ajout_travail
from pages.sidebar import sidebar


PAGES = {
    "Travaux en cours": travaux,
    "Ajouter un travail": ajout_travail,
}


selection = sidebar(list(PAGES.keys()))
page = PAGES[selection]
page.content()

