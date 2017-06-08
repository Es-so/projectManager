from Tkinter import *
from tkMessageBox import *
import sys

class typeView(object):
    """Type view"""
    def __init__(self, frame, app):
        self.frame = frame
    def switchView(self, view = 'typeView'):
        print view, 'in TypeView'
        self.app.switchView(view)
