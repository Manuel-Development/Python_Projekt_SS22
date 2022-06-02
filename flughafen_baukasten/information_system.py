#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"

########################################################################################################################

from datetime import datetime
import time
import traceback
from generator import FlugzeugGenerator
from flugzeug import Flugzeug
from src import get_project_root


class InformationSystem:
    bekannte_flugzeuge = []
    historie_flugzeuge = []

    queue_landen = []
    queue_parken = []
    queue_starten = []

    def __init__(self, flughafen):
        self.flughafen = flughafen
        self.flugzeug_generator = FlugzeugGenerator(flugzeug_klasse=Flugzeug,
                                                    daten_pool=(str(get_project_root()) + "\\ressources\\"))

    def flugzeug_erfassen(self):
        self._ueberpruefe_vorkommen_in_system(
            flugzeug=self.flugzeug_generator.flugzeuge_mit_zufaelligen_abstaenden_erzeugen())

    def _flugnummer_erzeugen(self, flugzeug):
        return ''.join(flugzeug.typ[:2] + str(100 + len(self.bekannte_flugzeuge)))

    def _ueberpruefe_vorkommen_in_system(self, flugzeug):
        if not (flugzeug.typ in self.bekannte_flugzeuge or
                flugzeug.gesellschaft in self.bekannte_flugzeuge):
            flugzeug.nummer = self._flugnummer_erzeugen(flugzeug=flugzeug)
            flugzeug_dict = {
                "Typ": flugzeug.typ,
                "Gesellschaft": flugzeug.gesellschaft,
                "Nummer": flugzeug.nummer,
            }

            print("Neues Flugzeug wurde in System aufgenommen:", flugzeug_dict)
            self.bekannte_flugzeuge.append(flugzeug_dict)

        self.queue_landen.append(flugzeug)

    def landung_durchfuehren(self):
        index, flugzeug = self._auswahl_ueber_index_treffen(queue=self.queue_landen, intent="Flugzeug ist gelandet")
        bahn = self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(
            flughafen_objekte=self.flughafen.bahnen,
            belegt=False)

        if bahn is not None:
            self.queue_parken.append(flugzeug)
            bahn.belegt = True
            bahn.landeflug_freigabe = True
            bahn.flugzeug = flugzeug

            flugzeug.bahn = bahn

            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf der Bahn {} gelandet.".format(index,
                                                                      flugzeug.typ,
                                                                      flugzeug.gesellschaft,
                                                                      flugzeug.nummer,
                                                                      bahn.nummer))
            flugzeug.ist_zeitpunkt_landung = datetime.now()
            time.sleep(3)

        else:
            self.queue_landen.insert(index, flugzeug)

            bahn.belegt = False
            bahn.landeflug_freigabe = False
            bahn.flugzeug = None

    def parken_durchfuehren(self):
        index, flugzeug = self._auswahl_ueber_index_treffen(queue=self.queue_parken, intent="Flugzeug wurde geparkt")
        parkplatz = self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(
            flughafen_objekte=self.flughafen.park_positionen,
            belegt=False)
        follow_me_fahrzeug = self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(
            flughafen_objekte=self.flughafen.follow_me_fahrzeuge,
            belegt=False)

        if (parkplatz and follow_me_fahrzeug and flugzeug) is not None:
            self.queue_starten.append(flugzeug)

            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf dem Parkplatz {} geparkt.".format(index,
                                                                          flugzeug.typ,
                                                                          flugzeug.gesellschaft,
                                                                          flugzeug.nummer,
                                                                          parkplatz.nummer))

            follow_me_fahrzeug.belegt = False
            follow_me_fahrzeug.flugzeug = flugzeug

            flugzeug.wird_gezogen = False
            flugzeug.ist_geparkt = True
            flugzeug.bahn.belegt = False
            flugzeug.bahn = None

            parkplatz.belegt = True
            parkplatz.flugzeug = flugzeug

        else:
            self.queue_parken.insert(index, flugzeug)

            follow_me_fahrzeug.belegt = False
            follow_me_fahrzeug.flugzeug = None

            flugzeug.wird_gezogen = False
            flugzeug.ist_geparkt = False

            parkplatz.belegt = False
            parkplatz.flugzeug = None

    def start_durchfuehren(self):
        index, flugzeug = self._auswahl_ueber_index_treffen(queue=self.queue_starten, intent="Flugzeug ist gestartet")
        bahn = self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(
            flughafen_objekte=self.flughafen.bahnen,
            belegt=False)
        follow_me_fahrzeug = self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(
            flughafen_objekte=self.flughafen.follow_me_fahrzeuge,
            belegt=False)

        if (flugzeug and bahn and follow_me_fahrzeug) is not None:

            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf der Bahn {} gestartet.".format(index,
                                                                       flugzeug.typ,
                                                                       flugzeug.gesellschaft,
                                                                       flugzeug.nummer,
                                                                       bahn.nummer))

            follow_me_fahrzeug.belegt = False
            follow_me_fahrzeug.flugzeug = None

            flugzeug.wird_gezogen = False
            flugzeug.parkplatz = None

        else:
            self.queue_starten.insert(index, flugzeug)

            follow_me_fahrzeug.belegt = False
            follow_me_fahrzeug.flugzeug = None

            flugzeug.wird_gezogen = False

            flugzeug.parkplatz.belegt = True

    def _auswahl_ueber_index_treffen(self, queue, intent):
        try:
            [print("{}: Typ:{}, Gesellschaft:{}, Nummer:{}".format(i, queue[i].typ,
                                                                   queue[i].gesellschaft,
                                                                   queue[i].nummer))
             for i in range(0, len(queue))]

            index = int(input("\nAuswahl über Index treffen: "))
            flugzeug = queue[index]

            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, Nummer:{}) "
                  "wurde ausgewählt.".format(index,
                                             flugzeug.typ,
                                             flugzeug.gesellschaft,
                                             flugzeug.nummer))
            time.sleep(3)
            queue.pop(index)

            self._flugzeug_historie_generieren(flugzeug=flugzeug, intent=intent)

            return index, flugzeug

        except (Exception,):
            traceback.print_exc()
            print("Ihre Auswahl war nicht gültig. Bitte treffen Sie eine Auswahl über einen gültigen Index")
            self._auswahl_ueber_index_treffen(queue=queue, intent=intent)

    def _uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(self, flughafen_objekte, belegt):
        try:
            [print("{}: Belegt:{}, Flugzeug:{}".format(objekt.nummer, objekt.belegt,
                                                       objekt.flugzeug))
             for objekt in flughafen_objekte if objekt.belegt == belegt]
            index = int(input("\nAuswahl über Index-Nummer treffen: "))

            for objekt in flughafen_objekte:
                if objekt.nummer == index:
                    print("{} mit der Nummer {} wurde ausgewählt.".format(objekt.defined_name, objekt.nummer))
                    time.sleep(3)
                    return objekt

            self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(flughafen_objekte=flughafen_objekte,
                                                                                belegt=belegt)

        except (Exception,):
            traceback.print_exc()
            self._uberpruefe_belegung_von_flughafen_objekten_und_treffe_auswahl(flughafen_objekte=flughafen_objekte,
                                                                                belegt=belegt)

    def flugzeug_historie_ausgeben(self):
        [print(historie_flug) for historie_flug in self.historie_flugzeuge]
        time.sleep(3)

    def _flugzeug_historie_generieren(self, flugzeug, intent):
        self.historie_flugzeuge.append({intent: flugzeug.status})




