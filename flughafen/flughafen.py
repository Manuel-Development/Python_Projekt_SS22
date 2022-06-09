########################################################################################################################
"""
flughafen.py: Hier liegt die "Flughafen-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################


class Flughafen:

    def __init__(self, bahn_klasse, park_position_klasse, lotse_klasse, name):
        self.name = name
        self.__bahn_klasse = bahn_klasse
        self.__park_position_klasse = park_position_klasse
        self.__lotse_klasse = lotse_klasse
        self.anzahl_bahnen = 4
        self.anzahl_park_positionen = 10
        self.anzahl_lotsen = 1
        self.bahnen = []
        self.parkplaetze = []
        self.lotsen = []
        [self._instanziieren(cls_ref=self.__bahn_klasse, nummer=_, cls_variable=self.bahnen,
                             instance_name="Bahn")
         for _ in range(self.anzahl_bahnen)]
        [self._instanziieren(cls_ref=self.__park_position_klasse, nummer=_, cls_variable=self.parkplaetze,
                             instance_name="Parkplatz")
         for _ in range(self.anzahl_park_positionen)]
        [self._instanziieren(cls_ref=self.__lotse_klasse, nummer=_, cls_variable=self.lotsen,
                             instance_name="Lotse")
         for _ in range(self.anzahl_lotsen)]

        print("*" * 150 + "\n"
              + self.name + "\n" +
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
                                                                                   name=instance_name),
                                                          standard=None)
        if instance_name is not None:
            cls_variable.append(instance_name)

    @staticmethod
    def __try_except_utility_methode(funktion, standard):
        try:
            return funktion()

        except (Exception,):
            return standard
