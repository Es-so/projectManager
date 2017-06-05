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

def projectList(root):
    pList = Listbox(root)
    pList.insert(1, "C")
    pList.insert(2, "Python")
    pList.insert(3, "Web client")
    pList.insert(4, "Web server")
    pList.insert(5, "Web client/server")
    return ({ "pList": pList, "pLen": 6 })

class mainView(object):
    """Main view"""
    def __init__(self, root):
        self.root = root
        self.root.config(menu=headerMenu(self.root, self.popup))
        self.label = Label(self.root, text="Select project types")
        self.label.pack()
        self.pl = projectList(self.root)
        self.pl['pList'].pack()
        self.okButton=Button(root, text="Ok", command=self.root.quit)
        self.okButton.pack()

    def popup(self):
        self.w = popupWindow(self.root)
        self.root.wait_window(self.w.top)
        self.pl['pList'].insert(self.pl['pLen'], self.w.value)
        self.pl['pLen'] += 1

    def entryValue(self):
        return self.w.value
