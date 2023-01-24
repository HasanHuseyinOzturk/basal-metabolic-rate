# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:52:02 2021

@author: hasan
"""

#from PyQt4 import uic

from PyQt5 import uic

with open('anaSayfa.py', 'w', encoding="utf-8") as fout:
   uic.compileUi('anaSayfa.ui', fout)