#!/usr/bin/env python
########################################################################################################################
"""
flugzeug.py: Description of what foobar does.
"""

__author__ = "Python SS22"
__copyright__ = "Copyright Group_2, SFM"
########################################################################################################################

from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent
