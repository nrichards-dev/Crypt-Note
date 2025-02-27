import sqlite3

DELETE_ROW = 'DELETE FROM notes WHERE note_id=(g?);'
ADD_ROW = 'INSERT INTO notes (encrypted_data, title, salt) VALUES (?, ?, ?);'
def connectDB():
    return sqlite3.connect('notes.db')

def add_row(connection, data, title, salt):
    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_ROW, (data, title, salt))

def remove_row(connection, id: int):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ROW, (id))

def get_row(connection, id):
    with connection:
        cursor = connection.cursor() 
        cursor.execute(f'SELECT note_id, encrypted_data, title, salt FROM notes WHERE note_id={id};')
        return cursor.fetchall()
    
def list_all(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM notes')
    return cursor.fetchall()

def create_row(connection, title):
    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_ROW, (None, title, None))