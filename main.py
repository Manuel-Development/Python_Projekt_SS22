########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

# Imports from Custom Module
from flughafen_baukasten import Flughafen
from flughafen_baukasten import Bahn
from flughafen_baukasten import Fahrzeug
from flughafen_baukasten import Lotse
from flughafen_baukasten import Parkplatz
from flughafen_baukasten import InformationSystem

# Imports from Custom Module
from flughafen_cmds import Kommandos

if __name__ == '__main__':
    flughafen = Flughafen(defined_name="Flughafen München",
                          bahn_klasse=Bahn,
                          follow_me_fahrzeug_klasse=Fahrzeug,
                          lotse_klasse=Lotse,
                          park_position_klasse=Parkplatz)

    information_system = InformationSystem(flughafen=flughafen)
    kommandos = Kommandos(information_system=information_system)
    lotse = Lotse(nummer=1, kommandos=kommandos)

    while True:
        lotse.entscheidung(input_cmd=kommandos.kommandos_zeigen())
