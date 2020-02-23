# -*- coding: utf-8 -*

import sys
import unicodedata
from importlib import reload

reload(sys)


class ParsingException(Exception):
    reason = ''
    
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'Error: ' + self.reason
