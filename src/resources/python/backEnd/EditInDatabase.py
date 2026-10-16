'''
File: CreateShow.py
Project: DevOps
Author: Dylan Greene
Created: 15/10/2026
Copyright (c) 2026 Dylan Greene
'''

from pathlib import Path
import sqlite3
import hashlib

DB_PATH = (
    Path(__file__).resolve().parents[2]
    / "databases"
    / "mockDatabase.db"
)


def createShow(root, name, seasons, channel, creator, rating, userId):
    from frontEnd.MainPage import createMainPage
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
            """
            INSERT INTO shows
                (user_id, name, seasons, channel, creator, rating)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (userId, name, seasons, channel, creator, rating)
        )

    conn.commit()
    conn.close()



    createMainPage(root, userId)  # Call createMainPage after creating the show


def editShow(root, showID, name, seasons, channel, creator, rating, userId):
    from frontEnd.MainPage import createMainPage

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        UPDATE shows
        SET name = ?, seasons = ?, channel = ?, creator = ?, rating = ?
        WHERE id = ?
        """,
        (name, seasons, channel, creator, rating, showID)
    )
    
    conn.commit()
    conn.close()

    createMainPage(root, userId)  # Call createMainPage after creating the show

def deleteShow(root,showID, userId):
    from frontEnd.MainPage import createMainPage
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
        
    cursor.execute(
        "DELETE FROM shows WHERE id = ?",
        (showID,)
    )
        
    conn.commit()
    conn.close()

    createMainPage(root, userId)  # Call createMainPage after creating the show
