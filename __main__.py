#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
import sys
from srcs.app import *

def init(root):
    root.wm_title("Project Manager v0")
    root.minsize(width=350, height=250)

if __name__ == "__main__":
    root = Tk()
    init(root)
    App(root)
    root.mainloop()
