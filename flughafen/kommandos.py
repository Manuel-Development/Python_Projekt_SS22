########################################################################################################################
"""
kommandos.py: Hier liegt die "Kommandos-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

import sys


class Kommandos:
    CMD = {
        "Flugzeug anlegen:": 1,
        "Flugzeug auswählen:": 2,
        "Historie darstellen": 3,
        "Simulation beenden:": 4
    }

    def __init__(self, information_system):
        self.information_system = information_system

    def kommandos_zeigen(self):
        print("\n")
        print("*" * 10 + "Auswahl-Menu" + "*" * 10)
        [print(key, item) for key, item in self.CMD.items()]
        print("*" * 32)
        print("\n")
        eingabe = input("Nächste Aktion: ")
        return eingabe

    def flugzeug_anlegen(self):
        self.information_system.flugzeug_anlegen()

    def flugzeug_auswaehlen(self):
        self.information_system.flugzeug_auswaehlen()

    def flug_historie_darstellen(self):
        self.information_system.flugzeug_historie_ausgeben()

    @staticmethod
    def information_system_beenden():
        sys.exit(0)

