########################################################################################################################
"""
lotse.py: Hier liegt die "Lotse-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################


class Lotse:

    def __init__(self, nummer, kommandos, name):
        self.name = name
        self.nummer = nummer
        self.kommandos = kommandos

    def entscheidung(self, input_cmd: str):
        if input_cmd == "1":
            self.kommandos.flugzeug_anlegen()

        elif input_cmd == "2":
            self.kommandos.flugzeug_auswaehlen()

        elif input_cmd == "3":
            self.kommandos.flugzeug_warteliste_auswaehlen()

        elif input_cmd == "4":
            self.kommandos.flug_historie_darstellen()

        elif input_cmd == "5":
            self.kommandos.information_system_beenden()
