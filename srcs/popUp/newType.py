from Tkinter import *
from tkMessageBox import *
import sys

class PopupWindow(object):
    def __init__(self,master='' ):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="New type")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
