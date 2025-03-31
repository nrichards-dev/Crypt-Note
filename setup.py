import sqlite3
from os import listdir, path
from secrets import token_bytes


def setup():
    # Store 16byte salt to file
    if ('passwd' not in listdir()) or (path.getsize('passwd') == 0):
        with open('passwd', 'w') as file:
            file.write(str(token_bytes(16)))
        file.close()

    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS notes 
                    (note_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    encrypted_data BLOB,
                    title TEXT NOT NULL,
                    salt BLOB,
                    hash BLOB)''')
    db.close()

    with open('setup_complete.flag', 'w') as file:
        file.write('1')
        file.close()
