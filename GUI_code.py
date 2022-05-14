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

       self.label_message2 = Label(self.window2, text=' ')
       self.label_message2.pack(side='top', pady=20)

       self.button_submit = Button(self.window2, text='SUBMIT', command=self.clicked)
       self.button_submit.pack(side='top')

   def clicked(self):
       passget = self.entry_up1.get()
       print(f'{t.status(passget)}')
       self.label_message1.config(text=f'{t.status(passget)}')

       if passget != 'too weak':
           site_window = Tk()
           site_window.geometry('250x230')
           site_window.resizable(False, False)
           self.window3 = site_window
