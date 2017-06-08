from Tkinter import *
from views.Main.view import *
from popUp.newType import *

Views = {
    'mainView': {
        'title': 'Main menu',
        'frame': {}
    },
    'typeView': {
        'title': 'Type menu',
        'frame': {}
    }
}

def topMenu(root, popup):
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label='New type', command=popup)
    fileMenu.add_command(label='Edit type', command=alert)
    menubar.add_cascade(label='Project', menu=fileMenu)
    return menubar

class App(object):
    """docstring for App"""
    def __init__(self, root):
        self.root = root
        self.root.config(menu=topMenu(root, self.popup))
        self.frames = Views
        self.frames = { view : {'frame' : Frame(root) , 'title' : Views[view]['title']} for view in Views }
        print (self.frames, Views)
        self.currentView = self.frames['mainView']['frame']
        self.currentView.grid(row=0)
        mainView(self.currentView, self)
        Button(self.root, text='main', command=self.switchView).grid(row=1)

    def switchView(self, view = 'mainView'):
        print view, 'in app'
        self.currentView.grid_forget()
        self.currentView = self.frames[view]['frame']
        self.currentView.grid(row=0)

    def popup(self):
        self.w = PopupWindow(self.root)
        self.root.wait_window(self.w.top)
        self.switchView('mainView')
        # self.pl['pList'].insert(self.pl['pLen'], self.w.value)
        # self.pl['pLen'] += 1

    def entryValue(self):
        return self.w.value
