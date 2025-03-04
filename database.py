import sqlite3

DELETE_ROW = 'DELETE FROM notes WHERE note_id=?;'
ADD_ROW = 'INSERT INTO notes (encrypted_data, title, salt) VALUES (?, ?, ?);'
GET_ROW = 'SELECT * FROM notes WHERE note_id=?;'
EDIT_DATA = 'UPDATE notes SET encrypted_data=? WHERE note_id=?;'
def connectDB():
    return sqlite3.connect('notes.db')

def edit_data(connection, newData, id):
    with connection:
        cursor = connection.cursor()
        cursor.execute(EDIT_DATA, (newData, id))


def create_row(connection, title):
    with connection:
        cursor = connection.cursor()
        cursor.execute(ADD_ROW, (None, title, None))

def remove_row(connection, id: int):
    with connection:
        cursor = connection.cursor()
        cursor.execute(DELETE_ROW, (id,))

# fix so it gets entire row information
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

