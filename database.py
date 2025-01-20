import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("./ascender_path.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           task TEXT NOT NULL
                           )
                    """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()


def add_task_to_db(task):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error assing task: {e}")
        finally:
            conn.close()

def get_all_tasks():
    conn = create_connection()
    tasks = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, task FROM tasks")
            tasks = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting tasks: {e}")
        finally:
            conn.close()
    return tasks

def remove_task_from_db(id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error removing task: {e}")
        finally:
            conn.close()

def clear_task_db():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error clearing all tasks: {e}")
        finally:
            conn.close()

def create_characters_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS characters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    level INTEGER NOT NULL,
                    strength INTEGER NOT NULL,
                    agility INTEGER NOT NULL,
                    intelligence INTEGER NOT NULL,
                    endurance INTEGER NOT NULL,
                    perception INTEGER NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating characters table: {e}")
        finally:
            conn.close()


def add_character(character_data):
    conn = create_connection()
    if conn is not None:
         try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO characters (name, level, strength, agility, intelligence, endurance, perception)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, character_data)
            conn.commit()
         except sqlite3.Error as e:
            print(f"Error adding character: {e}")
         finally:
            conn.close()

def get_all_characters():
    conn = create_connection()
    characters = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, level, strength, agility, intelligence, endurance, perception FROM characters")
            characters = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting characters: {e}")
        finally:
            conn.close()
    return characters

def remove_character(id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM characters WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
          print(f"Error removing character: {e}")
        finally:
          conn.close()