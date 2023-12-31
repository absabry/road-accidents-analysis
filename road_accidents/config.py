DATASET_PREFIX = "https://www.data.gouv.fr/fr/datasets/r/"
VEHICULE_PATH = f"{DATASET_PREFIX}/c9742921-4427-41e5-81bc-f13af8bc31a0"
CARACTERISTIQUES_PATH = f"{DATASET_PREFIX}/5fc299c0-4598-4c29-b74c-6a67b0cc27e7"

VEHICULE_COLS = [
    "Num_Acc",
    "id_vehicule",
    "num_vehicule",
    "sens_de_Circulation",
    "catV",
    "obstacle_fixe",
    "obstacle_mobile",
    "choc",
    "manoeuvre",
    "motor",
    "nb_occupants",
]

info_vehicules = {
    1: "Bicyclette",
    2: "Cyclomoteur <50cm3",
    3: "Voiturette (Quadricycle à moteur carrossé) (anciennement voiturette ou tricycle à moteur)",
    4: "Référence plus utilisée depuis 2006 (scooter immatriculé)",
    5: "Référence plus utilisée depuis 2006 (motocyclette)",
    6: "Référence plus utilisée depuis 2006 (side-car)",
    7: "VL seul",
    8: "Catégorie plus utilisée (VL + caravane)",
    9: "Catégorie plus utilisée (VL + remorque)",
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)",
    11: "Référence plus utilisée depuis 2006 (VU (10) + caravane)",
    12: "Référence plus utilisée depuis 2006 (VU (10) + remorque)",
    13: "PL seul 3,5T <PTCA <= 7,5T",
    14: "PL seul > 7,5T",
    15: "PL > 3,5T + remorque",
    16: "Tracteur routier seul",
    17: "Tracteur routier + semi-remorque",
    18: "Référence plus utilisée depuis 2006 (transport en commun)",
    19: "Référence plus utilisée depuis 2006 (tramway)",
    20: "Engin spécial",
    21: "Tracteur agricole",
    30: "Scooter < 50 cm3",
    31: "Motocyclette > 50 cm et <= 125 cm",
    32: "Scooter >50cm et<=125cm",
    33: "Motocyclette",
    34: "Scooer",
    35: "Quad",
    36: "Quad lourd > 50 cm (Quadricycle à moteur non carrossé)",
    37: "Autobus",
    38: "Autocar",
    39: "Train",
    40: "Tramway",
    99: "Autre véhicule",
}

obstacle_labels = {
    0: "inconnu_0",
    1: "Piéton",
    2: "Véhicule",
    4: "Véhicule sur rail",
    5: "Animal domestique 6",
    6: "Animal sauvage",
    9: "Autre",
    None: "inconnu",
}

obstacle_fixe_labels = {
    1: "Véhicule en stationnement",
    2: "Arbre",
    3: "Glissière métallique",
    4: "Glissière béton",
    5: "Autre glissière",
    6: "Bâtiment, mur, pile de pont",
    7: "Support de signalisation verticale ou poste d’appel d’urgence ",
    8: "Poteau",
    9: "Mobilier urbain",
    10: "Parapet",
    11: "Ilot, refuge, borne haute",
    12: "Bordure de trottoir",
    13: "Fossé, talus, paroi rocheuse",
    14: "Autre obstacle fixe sur chaussée",
    15: "Autre obstacle fixe sur trottoir ou accotement 16 – Sortie de chaussée sans obstacle",
}

meteo_labels = {
    1: "Normale",
    2: "Pluie légère",
    3: "Pluie forte",
    4: "Neige - grêle",
    5: "Brouillard - fumée",
    6: "Vent fort - tempête",
    7: "Temps éblouissant",
    8: "Temps couvert",
    9: "Autre",
}
