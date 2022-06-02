#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

import traceback


class Lotse:

    def __init__(self, nummer, kommandos, defined_name=None):
        if defined_name is None:
            (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
            defined_name = text[:text.find('=')].strip()
        self.defined_name = defined_name
        self.nummer = nummer
        self.kommandos = kommandos

    def entscheidung(self, input_cmd: str):
        if input_cmd == "1":
            self.kommandos.flugzeug_erfassen()

        elif input_cmd == "2":
            self.kommandos.flugzeug_landen()

        elif input_cmd == "3":
            self.kommandos.flugzeug_parken()

        elif input_cmd == "4":
            self.kommandos.flugzeug_starten()

        elif input_cmd == "5":
            self.kommandos.flug_historie_darstellen()

        elif input_cmd == "6":
            self.kommandos.information_system_beenden()
