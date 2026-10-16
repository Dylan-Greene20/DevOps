'''
File: MainPage.py
Project: DevOps
Author: Dylan Greene
Created: 16/10/2026
Copyright (c) 2026 Dylan Greene
'''

import tkinter as tk
from frontEnd.DeleteShowPage import deleteShowPage
from frontEnd.CreateShowPage import createShowPage
from frontEnd.EditShowPage import editShowPage
from backEnd.GetFromDatabase import getShowsForUser
def createMainPage(root, userID):
    for widget in root.winfo_children():
        widget.destroy()
    shows = getShowsForUser(userID)
    if(not shows):
        createShowPage(root, userID)
    else:
        mainPageLabel = tk.Label(root, text='Shows Viewed', font=('calibre', 20, 'bold'))
        showNameLabel = tk.Label(root, text='Name', font=('calibre', 10, 'bold'))
        showRatingLabel = tk.Label(root, text='Rating', font=('calibre', 10, 'bold'))
        createShowButton = tk.Button(root, text="Create Show", command=lambda: createShowPage(root, userID))
        mainPageLabel.grid(row=0,column=0)
        createShowButton.grid(row=0,column=10)

        showNameLabel.grid(row=1,column=0)
        showRatingLabel.grid(row=1,column=1)
        for show in shows:
            showName = tk.Label(root, text=show['name'], font=('calibre', 10, 'normal'))
            showRating = tk.Label(root, text=show['rating'], font=('calibre', 10, 'normal'))

            showAll = tk.Button(root, text="View Details", command=lambda showID=show['id']: showAll(show['channel'], show['creator'], show['seasons'], show['rating']))
            showEditButton = tk.Button(root, text="Edit", command=lambda showID=show['id']: editShowPage(root, showID, userID))
            showDeleteButton = tk.Button(root, text="Delete", command=lambda showID=show['id']: deleteShowPage(root, showID, userID))
            print(shows.index(show))
            showName.grid(row=shows.index(show)*2+2,column=0)   
            showRating.grid(row=shows.index(show)*2+2,column=1)
            showAll.grid(row=shows.index(show)*2+2,column=2)
            showEditButton.grid(row=shows.index(show)*2+2,column=3)
            showDeleteButton.grid(row=shows.index(show)*2+2,column=4)

def showAll(channel, creator, seasons, rating):
    # Implementation for showing all details of a show
    pass
