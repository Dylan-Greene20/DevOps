'''
File: LoginInPage.py
Project: DevOps
Author: Dylan Greene
Created: 14/10/2026
Copyright (c) 2026 Dylan Greene
'''
h
import tkinter as tk
from backEnd.LoginIn import *
root = tk.Tk()
root.geometry("600x400")

username = tk.StringVar()
password = tk.StringVar()

nameLabel = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
nameEntry = tk.Entry(root,textvariable = username, font=('calibre',10,'normal'))
nameEntry.bind(
    "<KeyRelease>",
    lambda event: removeWarnings(0))

passwordLabel = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
passwordInput=tk.Entry(root, textvariable = password, font = ('calibre',10,'normal'), show = '*')
passwordInput.bind(
    "<KeyRelease>",
    lambda event: removeWarnings(1))

signInButton = tk.Button(root, text="Log In", command=lambda: submit(username, password, root, passwordInput))
exitButton = tk.Button(root, text="Exit", command=root.destroy)


nameLabel.grid(row=0,column=0)
nameEntry.grid(row=1,column=0)
passwordLabel.grid(row=3,column=0)
passwordInput.grid(row=4,column=0)

signInButton.grid(row=6,column=0)
exitButton.grid(row=7,column=0)

root.mainloop()