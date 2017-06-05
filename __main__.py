#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import *
import sys
from srcs.views.Main.new import *
from srcs.views.Main.view import *

def raise_frame(frame):
    frame.tkraise()

def init(root):
    root.wm_title("Project Manager v0")
    root.minsize(width=350, height=150)

if __name__ == "__main__":
    root = Tk()
    init(root)
    mainView(root)
    root.mainloop()
