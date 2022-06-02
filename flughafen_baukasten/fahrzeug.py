#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

import traceback


class Fahrzeug:

    def __init__(self, nummer, defined_name=None):
        if defined_name is None:
            (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
            defined_name = text[:text.find('=')].strip()
        self.defined_name = defined_name
        self.nummer = nummer
        self._belegt = False
        self._flugzeug = None

    @property
    def belegt(self):
        return self._belegt

    @belegt.setter
    def belegt(self, value: bool):
        self._belegt = value

    @property
    def flugzeug(self):
        return self._flugzeug

    @flugzeug.setter
    def flugzeug(self, value: object):
        self._flugzeug = value
