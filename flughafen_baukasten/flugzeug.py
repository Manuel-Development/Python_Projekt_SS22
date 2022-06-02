#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################


class Flugzeug:

    def __init__(self, typ, gesellschaft, soll_zeitpunkt_landung,
                 ist_zeitpunkt_landung=None, soll_zeitpunkt_start=None, ist_zeitpunkt_start=None):
        self.typ = typ
        self.gesellschaft = gesellschaft
        self.nummer = "N.a."

        self.soll_zeitpunkt_landung = soll_zeitpunkt_landung
        self.ist_zeitpunkt_landung = ist_zeitpunkt_landung

        self.soll_zeitpunkt_start = soll_zeitpunkt_start
        self.ist_zeitpunkt_start = ist_zeitpunkt_start

        self._landet = False
        self._startet = False
        self._wird_gezogen = False
        self._ist_geparkt = False
        self._bahn = None
        self._parkplatz = None

    @property
    def landet(self):
        return self._landet

    @landet.setter
    def landet(self, value: bool):
        self._landet = value

    @property
    def startet(self):
        return self._startet

    @startet.setter
    def startet(self, value: bool):
        self._startet = value

    @property
    def wird_gezogen(self):
        return self._wird_gezogen

    @wird_gezogen.setter
    def wird_gezogen(self, value: bool):
        self._wird_gezogen = value

    @property
    def ist_geparkt(self):
        return self._ist_geparkt

    @ist_geparkt.setter
    def ist_geparkt(self, value: bool):
        self._ist_geparkt = value

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
    def status(self):
        return vars(self)
