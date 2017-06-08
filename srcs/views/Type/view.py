from Tkinter import *
from tkMessageBox import *
import sys
from new import *

def alert():
    showinfo("alerte", "todo")

def headerMenu(root, popup):
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="New type", command=popup)
    fileMenu.add_command(label="Edit type", command=alert)
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=root.quit)
    menubar.add_cascade(label="Project", menu=fileMenu)
    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="About", command=alert)
    menubar.add_cascade(label="Help", menu=helpMenu)
    return menubar

# todo -> json config file to set mplist
def projectList(root):
    pList = Listbox(root)
    pList.insert(1, "C")
    pList.insert(2, "Python")
    pList.insert(3, "Web client")
    pList.insert(4, "Web server")
    pList.insert(5, "Web client/server")
    return ({ "pList": pList, "pLen": 6 })

class typeView(object):
    """Main view"""
    def __init__(self, frame, app):
        self.frame = frame
        self.app = app
        self.label = Label(self.frame, text="Select project types")
        self.label.pack()
        self.pl = projectList(self.frame)
        self.pl['pList'].pack()
        self.okButton=Button(frame, text="Ok", command=self.switchView)
        self.okButton.pack()
    def switchView(self, view = 'typeView'):
        print view, 'in TypeView'
        self.app.switchView(view)
