'''
File: CreateShowPage.py
Project: DevOps
Author: Dylan Greene
Created: 15/10/2026
Copyright (c) 2026 Dylan Greene
'''

import tkinter as tk
from backEnd.EditInDatabase import deleteShow
from backEnd.GetFromDatabase import getShowDetails
from backEnd.Cancel import cancel
def deleteShowPage(root, showID, userId):
    for widget in root.winfo_children():
        widget.destroy()
    showDetails = getShowDetails(showID)

    name = tk.StringVar(value=showDetails["name"])
    seasons = tk.StringVar(value=showDetails["seasons"])
    channel = tk.StringVar(value=showDetails["channel"])
    creator = tk.StringVar(value=showDetails["creator"])
    rating = tk.IntVar(value=int(showDetails["rating"]))

    showEditLabel = tk.Label(root, text='Delete Show', font=('calibre', 20, 'bold'))

    showNameLabel = tk.Label(root, text='Name', font=('calibre', 10, 'bold'))
    showNameEntry = tk.Entry(root, textvariable=name, font=('calibre', 10, 'normal') , state='readonly')

    showSeasonsLabel = tk.Label(root, text='Seasons Amount', font=('calibre', 10, 'bold'))
    showSeasonsEntry = tk.Entry(root, textvariable=seasons, font=('calibre', 10, 'normal') , state='readonly')

    channelWatchedLabel = tk.Label(root, text='Channel Watched', font=('calibre', 10, 'bold'))
    channelWatchedEntry = tk.Entry(root, textvariable=channel, font=('calibre', 10, 'normal') , state='readonly')

    creatorLabel = tk.Label(root, text='Creator', font=('calibre', 10, 'bold'))
    creatorEntry = tk.Entry(root, textvariable=creator, font=('calibre', 10, 'normal') , state='readonly')

    ratingLabel = tk.Label(root, text='Rating', font=('calibre', 10, 'bold'))

    ratingInput = tk.Spinbox(
        root,
        from_=1,
        to=10,
        textvariable=rating,
        width=5
    )

    ratingInput.grid(row=8, column=0)

    deleteShowButton = tk.Button(root, text="Delete Show", command=lambda: deleteShowConfirmation(root, showID, userId))
    cancelButton = tk.Button(root, text="Cancel", command=lambda: cancel(root, userId))
    
    showEditLabel.grid(row=0, column=0)
    showNameLabel.grid(row=1, column=0)
    showNameEntry.grid(row=2, column=0)
    showSeasonsLabel.grid(row=3, column=0)
    showSeasonsEntry.grid(row=4, column=0)
    channelWatchedLabel.grid(row=5, column=0)
    channelWatchedEntry.grid(row=6, column=0)
    creatorLabel.grid(row=7, column=0)
    creatorEntry.grid(row=8, column=0)
    ratingLabel.grid(row=9, column=0)
    ratingInput.grid(row=10, column=0)
    deleteShowButton.grid(row=11, column=0)
    cancelButton.grid(row=11, column=1)
    root.mainloop()

def deleteShowConfirmation(root, showID, userId):
    for widget in root.winfo_children():
        widget.destroy()
    
    confirmationLabel = tk.Label(root, text='Are you sure you want to delete this show?', font=('calibre', 20, 'bold'))
    confirmationLabel.grid(row=0, column=0, columnspan=2)
    
    confirmButton = tk.Button(root, text="Yes", command=lambda: deleteShow(root, showID, userId))
    confirmButton.grid(row=1, column=0)
    
    cancelButton = tk.Button(root, text="No", command=lambda: deleteShowPage(root, showID, userId))
    cancelButton.grid(row=2, column=0)