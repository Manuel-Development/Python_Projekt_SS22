#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"

########################################################################################################################

import concurrent.futures
import json
import traceback
from os import walk
from random import randrange
from time import sleep
from datetime import datetime, timedelta

from flughafen_baukasten import Flugzeug


class FlugzeugGenerator:

    def __init__(self, flugzeug_klasse, daten_pool):
        self.flugzeug_klasse = flugzeug_klasse
        self.daten_pool = daten_pool
        self.json_daten = []

        try:
            _, _, self.json_dateien = next(walk(self.daten_pool), (None, None, []))

            with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                results = executor.map(self._lese_json_in_den_speicher, self.json_dateien)

            [self.json_daten.append(result) for result in results]

        except (Exception,):
            traceback.print_exc()

    def _lese_json_in_den_speicher(self, json_datei):
        try:
            with open(self.daten_pool + json_datei, encoding='utf-8') as datei:
                return json.load(datei)

        except (Exception,):
            traceback.print_exc()

    def _json_shuffler(self):
        return {
            "Typ": self.json_daten[1][randrange(len(self.json_daten[1]))],
            "Gesellschaft": self.json_daten[0][randrange(len(self.json_daten[0]))]
        }

    def flugzeuge_mit_zufaelligen_abstaenden_erzeugen(self, abstand=1):
        if abstand > 0:
            sleep(randrange(abstand))
            flugzeug_daten = self._json_shuffler()
            flugzeug = Flugzeug(typ=flugzeug_daten.get("Typ"),
                                gesellschaft=flugzeug_daten.get("Gesellschaft"),
                                soll_zeitpunkt_landung=datetime.now() + timedelta(minutes=5))

            print("*" * 150 + "\n" + "Flugzeug im Landeanflug\n" +
                  "       __|__\n"
                  "--o--o--(_)--o--o--\n"
                  + str(flugzeug_daten) + "\n"
                  + "*" * 150 + "\n")

            return flugzeug

        elif abstand <= 0:
            abstand = 1
            sleep(randrange(abstand))
            flugzeug_daten = self._json_shuffler()
            flugzeug = Flugzeug(typ=flugzeug_daten.get("Typ"),
                                gesellschaft=flugzeug_daten.get("Gesellschaft"),
                                soll_zeitpunkt_landung=datetime.now() + timedelta(minutes=5))

            print("*" * 150 + "\n" + "Flugzeug im Landeanflug\n" +
                  "       __|__\n"
                  "--o--o--(_)--o--o--\n"
                  + str(flugzeug_daten) + "\n"
                  + "*" * 150 + "\n")

            return flugzeug
