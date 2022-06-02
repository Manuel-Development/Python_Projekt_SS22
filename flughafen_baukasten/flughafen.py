#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

import traceback


class Flughafen:

    def __init__(self, bahn_klasse, park_position_klasse, lotse_klasse, follow_me_fahrzeug_klasse,
                 anzahl_bahnen=4, anzahl_park_positionen=8, anzahl_lotsen=1, anzahl_follow_me_fahrzeuge=4,
                 defined_name=None):

        if defined_name is None:
            (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
            defined_name = text[:text.find('=')].strip()
        self.defined_name = defined_name

        self.__bahn_klasse = bahn_klasse
        self.__park_position_klasse = park_position_klasse
        self.__lotse_klasse = lotse_klasse
        self.__follow_me_fahrzeug_klasse = follow_me_fahrzeug_klasse

        self.anzahl_bahnen = anzahl_bahnen
        self.anzahl_park_positionen = anzahl_park_positionen
        self.anzahl_lotsen = anzahl_lotsen
        self.anzahl_follow_me_fahrzeuge = anzahl_follow_me_fahrzeuge

        self.bahnen = []
        self.park_positionen = []
        self.lotsen = []
        self.follow_me_fahrzeuge = []

        [self._instanziieren(cls_ref=self.__bahn_klasse, nummer=_, cls_variable=self.bahnen,
                             instance_name="Bahn")
         for _ in range(self.anzahl_bahnen)]

        [self._instanziieren(cls_ref=self.__park_position_klasse, nummer=_, cls_variable=self.park_positionen,
                             instance_name="Parkplatz")
         for _ in range(self.anzahl_park_positionen)]

        [self._instanziieren(cls_ref=self.__lotse_klasse, nummer=_, cls_variable=self.lotsen,
                             instance_name="Lotse")
         for _ in range(self.anzahl_lotsen)]

        [self._instanziieren(cls_ref=self.__follow_me_fahrzeug_klasse, nummer=_, cls_variable=self.follow_me_fahrzeuge,
                             instance_name="Follow-Me-Fahrzeug")
         for _ in range(self.anzahl_follow_me_fahrzeuge)]

        print("*" * 150 + "\n"
              + self.defined_name + "\n" +
              "*" * 150 + "\n"
                          "__|__\n"
                          "\___/\n"
                          " | |\n"
                          " | |\n"
                          "_|_|______________\n"
                          "        /|\"\n"
                          "      */ | \*\n"
                          "      / -+- \"\n"
                          "  ---o--(_)--o---\n"
                          "    /  0 | 0  \"\n"
                          "  */     |     \*\n"
                          "  /      |      \"\n"
                          "*/       |       \*\n")

    def _generate_dictionary(self):
        return vars(self)

    def _instanziieren(self, cls_ref, nummer, cls_variable, instance_name):
        instance_name = self.__try_except_utility_methode(funktion=lambda: cls_ref(nummer=nummer,
                                                                                   defined_name=instance_name),
                                                          standard=None)
        if instance_name is not None:
            cls_variable.append(instance_name)

    @staticmethod
    def __try_except_utility_methode(funktion, standard):
        try:
            return funktion()

        except (Exception,):
            return standard
