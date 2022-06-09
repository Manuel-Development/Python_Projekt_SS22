########################################################################################################################
"""
flugzeug.py: Hier liegt die "Flugzeug-Klasse".
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################


class BahnPlatz:

    def __init__(self, nummer, name):
        self.name = name
        self.nummer = nummer
        self._flugzeug = None

    @property
    def flugzeug(self):
        return self._flugzeug

    @flugzeug.setter
    def flugzeug(self, value: object):
        self._flugzeug = value



