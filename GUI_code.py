import scores as t
from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_home = Frame(self.window)
        self.label_home1 = Label(self.frame_home, text='Welcome to my site! ')
        self.label_home2 = Label(self.frame_home, text='Please sign up!')
        self.frame_home.pack()
        self.label_home1.pack(side='top', pady=10)
        self.label_home2.pack(side='top')

        self.button_up = Button(self.window, text='Sign Up', command=self.sign_up)
        self.button_up.pack(padx=100, side='left')

    def sign_up(self):
        up_window = Tk()
        up_window.geometry('250x230')
        up_window.resizable(False, False)
        self.window2 = up_window

        self.frame_up = Frame(self.window2)
        self.label_up1 = Label(self.frame_up, text='Create a password')
        self.entry_up1 = Entry(self.frame_up)
        self.label_up2 = Label(self.frame_up, text='Create a username')
        self.entry_up2 = Entry(self.frame_up)
        self.frame_up.pack()
        self.label_up1.pack(side='top', pady=10)
        self.entry_up1.pack(side='top')
        self.label_up2.pack(side='top', pady=20)
        self.entry_up2.pack(side='top')

        self.label_message1 = Label(self.window2, text=' ')
        self.label_message1.pack(side='top', pady=20)

        self.button_submit = Button(self.window2, text='SUBMIT', command=self.clicked)
        self.button_submit.pack(side='top')

    def clicked(self):
        passget = self.entry_up1.get()
        print(f'{t.status(passget)}')
        self.label_message1.config(text=f'password is {t.status(passget)}')
        self.score = t.score(passget)

        if 'too weak' not in t.status(passget) and 'too short' not in t.status(passget) and 'too long' not in t.status(
                passget):
            site_window = Tk()
            site_window.geometry('150x150')
            site_window.resizable(False, False)
            self.window3 = site_window

            nameget = self.entry_up2.get()
            self.frame_end = Frame(self.window3)
            self.label_end = Label(self.frame_end, text=f'Welcome {nameget}!!!')
            self.frame_end.pack()
            self.label_end.pack()
