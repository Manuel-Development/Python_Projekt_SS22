########################################################################################################################
"""
information_system.py: Hier liegt die "InformationSystem-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"

########################################################################################################################
import traceback
from datetime import datetime as dt, timedelta
import datetime
import time
from .flugzeug import Flugzeug


class InformationSystem:
    bekannte_flugzeuge = []
    aktuelle_flugzeuge = []
    historie_flugzeuge = []

    def __init__(self, flughafen):
        self.flughafen = flughafen

    def flugzeug_anlegen(self):
        flugzeug = Flugzeug(
            typ=self._try_except_utility_methode(
                funktion=lambda: str(input("\nFlugzeug-Typ: ")),
                standard="Es wurde kein Typ definiert."),
            gesellschaft=self._try_except_utility_methode(
                funktion=lambda: str(input("\nFlugzeug-Gesellschaft: ")),
                standard="Es wurde keine Gesellschaft definiert."),
            zeit_soll=self._try_except_utility_methode(
                funktion=lambda: self._eingabe_uhrzeit(),
                standard=lambda: dt.now() + timedelta(minutes=10)))
        self._ueberpruefe_vorkommen_in_system(flugzeug)

    def flugzeug_auswaehlen(self):
        [print("{}: Das Flugzeug des Typs {} von der Gesellschaft {} mit der Nummer {} wartet auf {}.".format(i,
         self.aktuelle_flugzeuge[i].typ,
         self.aktuelle_flugzeuge[i].gesellschaft,
         self.aktuelle_flugzeuge[i].nummer,
         self.aktuelle_flugzeuge[i].naechster_schritt))
         for i in range(0, len(self.aktuelle_flugzeuge))]

        index = self._try_except_utility_methode(
            funktion=lambda: int(input("\nAuswahl über Index treffen: ")),
            standard=lambda: print("Das ist kein valider Index."))

        flugzeug = self.aktuelle_flugzeuge[index]
        print(">>{}: Das Flugzeug des Typs {} von der Gesellschaft {}"
              " mit der Nummer {} wartet auf {}.<< wurde ausgewählt\n".format(index,
                                                                              flugzeug.typ,
                                                                              flugzeug.gesellschaft,
                                                                              flugzeug.nummer,
                                                                              flugzeug.naechster_schritt))

        time.sleep(3)
        self._naechster_schritt_aufgrund_flugzeug_status(flugzeug=flugzeug, index=index)

    def flugzeug_historie_ausgeben(self):
        [print(historie_flug) for historie_flug in self.historie_flugzeuge]
        time.sleep(3)

    @staticmethod
    def _eingabe_uhrzeit():
        try:
            return (dt.today().strftime('%Y-%m-%d') +
                    " " +
                    datetime.datetime.strptime(input("\nSoll-Zeit [hhmm]: "), '%H%M').strftime('%H:%M'))

        except ValueError:
            print("Die eingegebene Uhrzeit entspricht nicht dem korrekten Format.\n"
                  "Das System setzt die Uhrzeit auf 10min in die Zukunft.")
            raise ValueError()

    def _flugnummer_erzeugen(self, flugzeug):
        return ''.join(flugzeug.typ[:2] + str(100 + len(self.aktuelle_flugzeuge)))

    def _ueberpruefe_vorkommen_in_system(self, flugzeug):
        if len(self.bekannte_flugzeuge) > 0:
            for bekanntes_flugzeug in self.bekannte_flugzeuge:
                if not (flugzeug.typ == bekanntes_flugzeug.typ or
                        flugzeug.gesellschaft == bekanntes_flugzeug.gesellschaft):
                    flugzeug.nummer = self._flugnummer_erzeugen(flugzeug=flugzeug)
                    print("\n       __|__\n"
                          "--o--o--(_)--o--o-- Ein neues Flugzeug wurde im System aufgenommen: "
                          "Typ:{}, Gesellschaft:{}, Nummer:{}, Soll-Zeit-Landung:{} Uhr\n".format(flugzeug.typ,
                                                                                                  flugzeug.gesellschaft,
                                                                                                  flugzeug.nummer,
                                                                                                  flugzeug.zeit_soll))
                    self.aktuelle_flugzeuge.append(flugzeug)
                    self.bekannte_flugzeuge.append(flugzeug)
                    time.sleep(3)
                else:
                    print("\nDas von Ihnen eingegebene Flugzeug existiert bereits.\n"
                          "Bitte geben Sie etwas anderes ein.")

        else:
            flugzeug.nummer = self._flugnummer_erzeugen(flugzeug=flugzeug)
            print("\n       __|__\n"
            "--o--o--(_)--o--o-- Ein neues Flugzeug wurde im System aufgenommen: "
            "Typ:{}, Gesellschaft:{}, Nummer:{}, Soll-Zeit-Landung:{} Uhr\n".format(flugzeug.typ,
                                                                                    flugzeug.gesellschaft,
                                                                                    flugzeug.nummer,
                                                                                    flugzeug.zeit_soll))
            self.aktuelle_flugzeuge.append(flugzeug)
            self.bekannte_flugzeuge.append(flugzeug)
            time.sleep(3)


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

    def _manuelle_entscheidung(self, flughafen_objekte, flugzeug, belegen):

        for i in range(0, len(flughafen_objekte)):
            if flughafen_objekte[i].flugzeug is None and belegen:
                print(str(i) + ": " + "{} {} ist verfügbar.".format(flughafen_objekte[i].name,
                                                                    str(flughafen_objekte[i].nummer)))
            elif flughafen_objekte[i].flugzeug is not None and not belegen:
                print(str(i) + ": " + "{} {} ist verfügbar.".format(flughafen_objekte[i].name,
                                                                    str(flughafen_objekte[i].nummer)))

        index = self._try_except_utility_methode(
            funktion=lambda: int(input("\nAuswahl über Index treffen: ")),
            standard=lambda: print("Das ist kein valider Index."))

        self._flugzeug_historie_generieren(flugzeug=flugzeug, intent=flugzeug.naechster_schritt)

        if belegen:
            flughafen_objekte[index].flugzeug = flugzeug
            return flughafen_objekte[index]

        elif not belegen:
            return flughafen_objekte[index]
        return None

    def _flugzeug_landen(self, flugzeug, index):
        bahn = self._try_except_utility_methode(
            funktion=lambda: self._manuelle_entscheidung(
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
            flugzeug.zeit_ist = dt.now()
            flugzeug.bahn = bahn
            flugzeug.gelandet = True
            flugzeug.naechster_schritt = "einparken"
            time.sleep(3)

        else:
            print("Es konnte keine freie Landebahn gefunden werden."
                  "\nSie müssen erst ein Flugzeug einparken.")

    def _flugzeug_einparken(self, flugzeug, index):
        parkplatz = self._try_except_utility_methode(
            funktion=lambda: self._manuelle_entscheidung(
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
            flugzeug.naechster_schritt = "ausparken"
            time.sleep(3)

        else:
            print("Es konnte keine freier Parkplatz gefunden werden."
                  "\nSie müssen erst ein Flugzeug ausparken.")
        print("yes")

    def _flugzeug_ausparken(self, flugzeug, index):
        bahn = self._try_except_utility_methode(
            funktion=lambda: self._manuelle_entscheidung(
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
                funktion=lambda: self._eingabe_uhrzeit(),
                standard=dt.now() + timedelta(minutes=10))
            flugzeug.parkplatz = None
            flugzeug.gestartet = True
            flugzeug.gelandet = False
            flugzeug.naechster_schritt = "starten"
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
        flugzeug.zeit_ist = dt.now()
        self.aktuelle_flugzeuge.pop(index)

        print("Das Flugzeug ist gestartet und kann nicht mehr ausgewählt werden.")
        time.sleep(3)

    def _flugzeug_historie_generieren(self, flugzeug, intent):
        self.historie_flugzeuge.append({intent: flugzeug.status})

    @staticmethod
    def _try_except_utility_methode(funktion, standard):
        try:
            return funktion()

        except (Exception,):
            traceback.print_exc()
            try:
                return standard()

            except (Exception, ):
                pass
