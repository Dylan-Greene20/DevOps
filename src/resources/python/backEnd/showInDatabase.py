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


def createShow(name, seasons, channel, creator, rating):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO shows (name, seasons, channel, creator, rating) VALUES (?, ?, ?, ?, ?)",
        (name, seasons, channel, creator, rating)
    )
    conn.commit()
    conn.close()

    print(f"Show '{name}' created successfully with {seasons} seasons, channel '{channel}', creator '{creator}', and rating {rating}.")