import sqlite3

def get_task(id):
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    if id is None:
        my_cursor.execute(f'SELECT * FROM tasks;')
    else:
        my_cursor.execute(f'SELECT * FROM tasks WHERE id=="{id}";')
    result = my_cursor.fetchall()
    con.close()
    return result

def count_tasks():
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    my_cursor.execute(f'''SELECT COUNT(*) FROM tasks;''')
    result = my_cursor.fetchall()
    con.close()
    return result

def add_task(id, title, description, time, status):
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    my_cursor.execute(f'''INSERT INTO tasks(id, title, description, time, status) 
                      VALUES("{id}", "{title}", "{description}", "{time}", "{status}");''')
    con.commit()
    con.close()

def update_task(id, title, description, time, status):
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    my_cursor.execute(f'UPDATE tasks SET(title, description, time, status) = ("{title}", "{description}", "{time}", "{status}") WHERE id=="{id}";')
    con.commit()
    con.close()

def delete_task(id):
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    my_cursor.execute(f'DELETE FROM tasks WHERE id=="{id}";')
    con.commit()
    con.close()

def search_task(id):
    con = sqlite3.connect('app/todo.db')
    my_cursor = con.cursor()
    my_cursor.execute(f'SELECT * FROM tasks WHERE id=="{id}";')
    result = my_cursor.fetchall()
    con.close()
    if len(result)>0:
        return True
    else:
        return False

