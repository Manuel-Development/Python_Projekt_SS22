########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
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
        return vars(self)
