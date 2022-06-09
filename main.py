########################################################################################################################
"""
main.py: Über diese Datei wird das Spiel gestartet/ausgeführt.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"

########################################################################################################################

# Imports from Custom Module
from flughafen.flughafen import Flughafen
from flughafen.lotse import Lotse
from flughafen.bahnplatz import BahnPlatz
from flughafen.information_system import InformationSystem
from flughafen.kommandos import Kommandos


def main():
    kommandos = Kommandos(information_system=InformationSystem(flughafen=Flughafen(name="Flughafen München",
                                                               bahn_klasse=BahnPlatz,
                                                               park_position_klasse=BahnPlatz,
                                                               lotse_klasse=Lotse)))
    lotse = Lotse(name="Horst", nummer=1, kommandos=kommandos)

    while True:
        lotse.entscheidung(input_cmd=kommandos.kommandos_zeigen())


if __name__ == '__main__':
    main()
