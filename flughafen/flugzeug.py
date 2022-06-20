########################################################################################################################
"""
flugzeug.py: Hier liegt die "Flugzeug-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"


########################################################################################################################


class Flugzeug:

    def __init__(self, typ, gesellschaft, zeit_soll):
        self.typ = typ
        self.gesellschaft = gesellschaft
        self.nummer = "N.a."
        self._zeit_soll = zeit_soll
        self._zeit_ist = None
        self._bahn = None
        self._parkplatz = None
        self._naechster_schritt = "landen"
        self._gelandet = False
        self._gestartet = False

    @property
    def zeit_soll(self):
        return self._zeit_soll

    @zeit_soll.setter
    def zeit_soll(self, value: int):
        self._zeit_soll = value

    @property
    def zeit_ist(self):
        return self._zeit_ist

    @zeit_ist.setter
    def zeit_ist(self, value: int):
        self._zeit_ist = value

    @property
    def bahn(self):
        return self._bahn

    @bahn.setter
    def bahn(self, value: object):
        self._bahn = value

    @property
    def parkplatz(self):
        return self._parkplatz

    @parkplatz.setter
    def parkplatz(self, value: object):
        self._parkplatz = value

    @property
    def naechster_schritt(self):
        return self._naechster_schritt

    @naechster_schritt.setter
    def naechster_schritt(self, value: str):
        self._naechster_schritt = value

    @property
    def gelandet(self):
        return self._gelandet

    @gelandet.setter
    def gelandet(self, value: bool):
        self._gelandet = value

    @property
    def gestartet(self):
        return self._gestartet

    @gestartet.setter
    def gestartet(self, value: bool):
        self._gestartet = value

    @property
    def status(self):
        status = {
            "Typ": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=self.typ)),
                                                     standard="N.a."),
            "Gesellschaft": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=self.gesellschaft)),
                                                              standard="N.a."),
            "Flug.-nr": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=self.nummer)),
                                                          standard="N.a."),
            "Soll-Zeit": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=self.zeit_soll)),
                                                           standard="N.a."),
            "Ist-Zeit": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=self.zeit_ist)),
                                                          standard="N.a."),
            "Bahn": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=str(self.bahn.name) + " " + str(self.bahn.nummer))),
                                                      standard="N.a."),
            "Parkplatz": self.__try_except_utility_methode(funktion=lambda:
            str(self.__fuelle_leere_werte(variable=str(self.parkplatz.name) + " " + str(self.parkplatz.nummer))),
                                                           standard="N.a."),
        }
        return status

    @staticmethod
    def __fuelle_leere_werte(variable):
        if variable is not None:
            return variable

        else:
            return "N.a."

    @staticmethod
    def __try_except_utility_methode(funktion, standard):
        try:
            return funktion()

        except (Exception,):
            return standard
