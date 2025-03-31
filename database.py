import sqlite3

DELETE_ROW = 'DELETE FROM notes WHERE note_id=?;'
ADD_ROW = 'INSERT INTO notes (encrypted_data, title, salt) VALUES (?, ?, ?);'
GET_ROW = 'SELECT * FROM notes WHERE note_id=?;'
EDIT_DATA = 'UPDATE notes SET encrypted_data=? WHERE note_id=?;'
EDIT_HASH = 'UPDATE notes SET hash=? WHERE note_id=?;'
def connectDB():
    return sqlite3.connect('notes.db')

def edit_data(connection, newData, id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(EDIT_DATA, (newData, id))

def edit_hash(connection, newHash, id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(EDIT_HASH, (newHash, id))

def create_row(connection, title, data=None, salt=None):
    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_ROW, (data, title, salt))

def remove_row(connection, id: int):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ROW, (id,))

def get_salt(connection,id):
    with connection:
        cursor = connection.cursor() 
        cursor.execute(GET_ROW, (id,))
        return cursor.fetchone()[3]
    
def get_row(connection, id):
    with connection:
        cursor = connection.cursor() 
        cursor.execute(GET_ROW, (id,))
        return cursor.fetchone()
    
def list_all(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM notes')
    return cursor.fetchall()


