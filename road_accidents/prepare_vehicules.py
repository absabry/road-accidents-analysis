import pandas as pd
from road_accidents.config import (
    VEHICULE_COLS,
    VEHICULE_PATH,
    info_vehicules,
    obstacle_labels,
    obstacle_fixe_labels,
)


def read_vehicules():
    """Read vehiculesfrom the web and add labels"""
    vehicules = pd.read_csv(VEHICULE_PATH, encoding="utf-8", sep=";")
    vehicules.columns = VEHICULE_COLS
    vehicules["label_vehicule"] = vehicules.catV.map(info_vehicules)
    vehicules["label_obstacle_mobile"] = vehicules.obstacle_mobile.map(obstacle_labels)
    vehicules["label_obstacle_fixe"] = vehicules.obstacle_fixe.map(obstacle_fixe_labels)
    return vehicules
