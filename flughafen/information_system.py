########################################################################################################################
"""
information_system.py: Hier liegt die "InformationSystem-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"

########################################################################################################################

from datetime import datetime, timedelta
import time
from .flugzeug import Flugzeug


class InformationSystem:
    bekannte_flugzeuge = []
    registrierte_flugzeuge = []
    wartelist_landen = []
    historie_flugzeuge = []

    def __init__(self, flughafen):
        self.flughafen = flughafen

    def flugzeug_anlegen(self):
        flugzeug = Flugzeug(
            typ=self._try_except_utility_methode(
                funktion=lambda: str(input("\nFlugzeug-Typ:")),
                standard="Es wurde kein Typ definiert."),
            gesellschaft=self._try_except_utility_methode(
                funktion=lambda: str(input("\nFlugzeug-Gesellschaft:")),
                standard="Es wurde keine Gesellschaft definiert."),
            zeit_soll=self._try_except_utility_methode(
                funktion=lambda: int(input("\nSoll-Zeit:")),
                standard=datetime.now() + timedelta(5)))
        self._ueberpruefe_vorkommen_in_system(flugzeug)

    def flugzeug_auswaehlen(self):
        [print("{}: Typ:{}, Gesellschaft:{}, Nummer:{}".format(i, self.registrierte_flugzeuge[i].typ,
                                                               self.registrierte_flugzeuge[i].gesellschaft,
                                                               self.registrierte_flugzeuge[i].nummer))
         for i in range(0, len(self.registrierte_flugzeuge))]

        index = self._try_except_utility_methode(
            funktion=lambda: int(input("\nAuswahl über Index treffen:")),
            standard="Das ist kein valider Index.")

        try:
            flugzeug = self.registrierte_flugzeuge[index]
            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, Nummer:{}) "
                  "wurde ausgewählt.".format(index,
                                             flugzeug.typ,
                                             flugzeug.gesellschaft,
                                             flugzeug.nummer))
            time.sleep(3)
            self._naechster_schritt_aufgrund_flugzeug_status(flugzeug=flugzeug, index=index)

        except (Exception,):
            print("Das ist kein valider Index.")
            time.sleep(3)

    def flugzeug_warteliste_auswaehlen(self):
        [print("{}: Typ:{}, Gesellschaft:{}, Nummer:{}".format(i, self.wartelist_landen[i].typ,
                                                               self.wartelist_landen[i].gesellschaft,
                                                               self.wartelist_landen[i].nummer))
         for i in range(0, len(self.wartelist_landen))]

        index = self._try_except_utility_methode(
            funktion=lambda: int(input("\nAuswahl über Index treffen:")),
            standard="Das ist kein valider Index.")

        try:
            flugzeug = self.registrierte_flugzeuge[index]
            print("Das Flugzeug ({}: Typ:{}, Gesellschaft:{}, Nummer:{}) "
                  "wurde ausgewählt.".format(index,
                                             flugzeug.typ,
                                             flugzeug.gesellschaft,
                                             flugzeug.nummer))
            time.sleep(3)
            self._naechster_schritt_aufgrund_flugzeug_status(flugzeug=flugzeug, index=index)

        except (Exception,):
            print("Das ist kein valider Index.")
            time.sleep(3)

    def flugzeug_historie_ausgeben(self):
        [print(historie_flug) for historie_flug in self.historie_flugzeuge]
        time.sleep(3)

    def _flugnummer_erzeugen(self, flugzeug):
        return ''.join(flugzeug.typ[:2] + str(100 + len(self.registrierte_flugzeuge)))

    def _ueberpruefe_vorkommen_in_system(self, flugzeug):
        if not (flugzeug.typ in self.bekannte_flugzeuge or
                flugzeug.gesellschaft in self.bekannte_flugzeuge):
            flugzeug.nummer = self._flugnummer_erzeugen(flugzeug=flugzeug)
            print("       __|__\n"
                  "--o--o--(_)--o--o-- Neues Flugzeug wurde in System aufgenommen: "
                  "Typ:{}, Gesellschaft:{}, Nummer:{}\n".format(flugzeug.typ,
                                                                flugzeug.gesellschaft,
                                                                flugzeug.nummer))
            self.registrierte_flugzeuge.append(flugzeug)
            self.bekannte_flugzeuge.append(flugzeug)
            time.sleep(3)
            self._naechster_schritt_aufgrund_flugzeug_status(flugzeug, index=len(self.registrierte_flugzeuge))
        else:
            print("Das von Ihnen eingegebene Flugzeug existiert bereits. Bitte geben Sie etwas anderes ein.")

    def _naechster_schritt_aufgrund_flugzeug_status(self, flugzeug, index):
        if flugzeug.bahn is None and flugzeug.parkplatz is None:
            self._flugzeug_landen(flugzeug, index)

        elif flugzeug.bahn is not None and \
                flugzeug.parkplatz is None and \
                flugzeug.gelandet:
            self._flugzeug_einparken(flugzeug, index)

        elif flugzeug.bahn is None and \
                flugzeug.parkplatz is not None:
            self._flugzeug_ausparken(flugzeug, index)

        elif flugzeug.bahn is not None and \
                flugzeug.parkplatz is None and \
                flugzeug.gestartet:
            self._flugzeug_starten(flugzeug, index)

        print("Bahnen")
        for test in self.flughafen.bahnen:
            print(test.flugzeug)

        print("Parkplätze")
        for test in self.flughafen.parkplaetze:
            print(test.flugzeug)

    @staticmethod
    def _automatische_entscheidung(flughafen_objekte, flugzeug, belegen):
        for flughafen_objekt in flughafen_objekte:
            if flughafen_objekt.flugzeug is None and belegen:
                flughafen_objekt.flugzeug = flugzeug
                return flughafen_objekt

            elif flughafen_objekt.flugzeug is not None and not belegen:
                return flughafen_objekt
        return None

    def _flugzeug_landen(self, flugzeug, index):
        bahn = self._try_except_utility_methode(
            funktion=lambda: self._automatische_entscheidung(
                flughafen_objekte=self.flughafen.bahnen,
                flugzeug=flugzeug,
                belegen=True),
            standard=None)

        if bahn is not None:
            print("Das Flugzeug ({} Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf der Bahn {} gelandet.".format(index,
                                                                      flugzeug.typ,
                                                                      flugzeug.gesellschaft,
                                                                      flugzeug.nummer,
                                                                      bahn.nummer))
            flugzeug.zeit_ist = datetime.now()
            flugzeug.bahn = bahn
            flugzeug.gelandet = True
            self._flugzeug_historie_generieren(flugzeug=flugzeug, intent="LANDEN")
            time.sleep(3)

        else:

            self.wartelist_landen.append(flugzeug)
            print("Es konnte keine freie Landebahn gefunden werden."
                  "\nSie müssen erst ein Flugzeug einparken.")

    def _flugzeug_einparken(self, flugzeug, index):
        parkplatz = self._try_except_utility_methode(
            funktion=lambda: self._automatische_entscheidung(
                flughafen_objekte=self.flughafen.parkplaetze,
                flugzeug=flugzeug,
                belegen=True),
            standard=None)

        if parkplatz is not None:
            print("Das Flugzeug ({} Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf dem Parkplatz {} geparkt.".format(index,
                                                                          flugzeug.typ,
                                                                          flugzeug.gesellschaft,
                                                                          flugzeug.nummer,
                                                                          parkplatz.nummer))
            flugzeug.bahn.flugzeug = None
            flugzeug.bahn = None
            flugzeug.parkplatz = parkplatz
            self._flugzeug_historie_generieren(flugzeug=flugzeug, intent="EINPARKEN")
            time.sleep(3)

        else:
            print("Es konnte keine freier Parkplatz gefunden werden."
                  "\nSie müssen erst ein Flugzeug ausparken.")

    def _flugzeug_ausparken(self, flugzeug, index):
        bahn = self._try_except_utility_methode(
            funktion=lambda: self._automatische_entscheidung(
                flughafen_objekte=self.flughafen.bahnen,
                flugzeug=flugzeug,
                belegen=True),
            standard=None)
        if bahn is not None:
            print("Das Flugzeug ({} Typ:{}, Gesellschaft:{}, "
                  "Nummer:{}) wurde auf der Bahn {} zum Starten aufgerufen.".format(index,
                                                                                    flugzeug.typ,
                                                                                    flugzeug.gesellschaft,
                                                                                    flugzeug.nummer,
                                                                                    bahn.nummer))
            flugzeug.parkplatz.flugzeug = None
            flugzeug.parkplatz = None
            flugzeug.bahn = bahn
            flugzeug.zeit_soll = self._try_except_utility_methode(
                funktion=lambda: int(input("\nSoll-Zeit:")),
                standard=datetime.now() + timedelta(5))
            flugzeug.parkplatz = None
            flugzeug.gestartet = True
            flugzeug.gelandet = False
            self._flugzeug_historie_generieren(flugzeug=flugzeug, intent="AUSPARKEN")
            time.sleep(3)

        else:
            print("Es konnte keine freie Startbahn gefunden werden."
                  "\nSie müssen erst ein Flugzeug einparken.")

    def _flugzeug_starten(self, flugzeug, index):
        print("Das Flugzeug ({} Typ:{}, Gesellschaft:{}, "
              "Nummer:{}) wurde auf der Bahn {} gestartet.".format(index,
                                                                   flugzeug.typ,
                                                                   flugzeug.gesellschaft,
                                                                   flugzeug.nummer,
                                                                   flugzeug.bahn.nummer))
        flugzeug.bahn.flugzeug = None
        flugzeug.bahn = None
        flugzeug.zeit_ist = datetime.now()
        self.registrierte_flugzeuge.pop(index)
        self._flugzeug_historie_generieren(flugzeug=flugzeug, intent="STARTEN")
        time.sleep(3)

        print("Das Flugzeug ist gestartet und kann nicht mehr ausgewählt werden.")

    def _flugzeug_historie_generieren(self, flugzeug, intent):
        self.historie_flugzeuge.append({intent: flugzeug.status})

    @staticmethod
    def _try_except_utility_methode(funktion, standard):
        try:
            return funktion()
        except (Exception,):
            return standard
