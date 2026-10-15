'''
File: CreateShowPage.py
Project: DevOps
Author: Dylan Greene
Created: 15/10/2026
Copyright (c) 2026 Dylan Greene
'''

import tkinter as tk
from backEnd.showInDatabase import createShow
def createShowPage(root):
    for widget in root.winfo_children():
        widget.destroy()

    showCreateLabel = tk.Label(root, text='Create Show', font=('calibre', 20, 'bold'))

    showNameLabel = tk.Label(root, text='Name', font=('calibre', 10, 'bold'))
    showNameEntry = tk.Entry(root, font=('calibre', 10, 'normal'))

    showSeasonsLabel = tk.Label(root, text='Seasons Amount', font=('calibre', 10, 'bold'))
    showSeasonsEntry = tk.Entry(root, font=('calibre', 10, 'normal'))

    channelWatchedLabel = tk.Label(root, text='Channel Watched', font=('calibre', 10, 'bold'))
    channelWatchedEntry = tk.Entry(root, font=('calibre', 10, 'normal'))

    creatorLabel = tk.Label(root, text='Creator', font=('calibre', 10, 'bold'))
    creatorEntry = tk.Entry(root, font=('calibre', 10, 'normal'))

    ratingLabel = tk.Label(root, text='Rating', font=('calibre', 10, 'bold'))

    rating = tk.IntVar(value=1)

    ratingInput = tk.Spinbox(
        root,
        from_=1,
        to=10,
        textvariable=rating,
        width=5
    )

    ratingInput.grid(row=8, column=0)

    createShowButton = tk.Button(root, text="Create Show", command=lambda: createShow(
        showNameEntry.get(),
        showSeasonsEntry.get(),
        channelWatchedEntry.get(),
        creatorEntry.get(),
        rating.get()
    ))
    cancelButton = tk.Button(root, text="Cancel", command=lambda: cancelCreateShow(root))
    
    showCreateLabel.grid(row=0, column=0)
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
    createShowButton.grid(row=11, column=0)
    cancelButton.grid(row=11, column=1)
    root.mainloop()