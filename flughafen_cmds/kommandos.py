#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

import sys


class Kommandos:
    CMD = {
        "Flugzeug erfassen:": 1,
        "Flugzeug landen:": 2,
        "Flugzeug parken:": 3,
        "Flugzeug starten:": 4,
        "Historie darstellen": 5,
        "Simulation beenden:": 6
    }

    def __init__(self, information_system):
        self.information_system = information_system

    def kommandos_zeigen(self):
        print("\n")
        print("*" * 10 + "Auswahl-Menu" + "*" * 10)
        [print(key, item) for key, item in self.CMD.items()]
        print("*" * 32)
        print("\n")
        return input("Nächste Aktion: ")

    def flugzeug_erfassen(self):
        self.information_system.flugzeug_erfassen()

    def flugzeug_landen(self):
        self.information_system.landung_durchfuehren()

    def flugzeug_parken(self):
        self.information_system.parken_durchfuehren()

    def flugzeug_starten(self):
        self.information_system.start_durchfuehren()

    def flug_historie_darstellen(self):
        self.information_system.flugzeug_historie_ausgeben()

    @staticmethod
    def information_system_beenden():
        sys.exit(0)
