'''
File: databaseModel.py
Project: DevOps
Author: Dylan Greene
Created: 14/10/2026
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

def singIn(username, password):
        # Find the user by username
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
            (username,)
    )
    result = cursor.fetchone()

    print(result)
    conn.close()

    if result is None:
        return False

    hashedPassword = hashlib.sha256(
        password.encode()
    ).hexdigest()

    if hashedPassword == result[0]:
        return True
    else:
        return False

def getUserId(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return None

    return result[0]

def getShowDetails(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM shows WHERE id = ?",
        (id,)
    )
    result = cursor.fetchone()
    conn.close()

    if result is None:
        return None

    return {
        "id": result[0],
        "user_id": result[1],
        "name": result[2],
        "seasons": result[3],
        "channel": result[4],
        "creator": result[5],
        "rating": result[6]
    }
