import sqlite3

# establish connection to the database
def create_connection():
    conn = None # initialize connection as None
    try:
        conn = sqlite3.connect("./ascender_path.db") # attempt to connect to the database
    except sqlite3.Error as e: # catch any errors on the connection
        print(f"Error connecting to database: {e}") # print the error to the console
    return conn # return the connection, may be None if an error occurred

# create a table if not exists
def create_table():
    conn = create_connection() # call the create connection to try to connect to the database
    if conn is not None: # verify if the connection is valid (not None)
        try:
            cursor = conn.cursor() # create a cursor object to execute SQL commands
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           task TEXT NOT NULL
                           )
                    """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}") # catches errors and prints them to the console
        finally:
            conn.close()

def add_task_to_db(task):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,)) # sql insert query
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error assing task: {e}")
        finally:
            conn.close()

def get_all_tasks():
    conn = create_connection()
    tasks = [] # inicialize the tasks array
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, task FROM tasks") # sql select alll
            tasks = cursor.fetchall()# get the result from the query
        except sqlite3.Error as e:
            print(f"Error getting tasks: {e}")
        finally:
            conn.close()
    return tasks # return the result

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


# CHARACTER CREATION
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

def add_character_to_db(character_data):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                    INSERT INTO characters(name, level, strength, agility, intelligence, endurance, perception)
                    VALUES(?, ?, ?, ?, ?, ?, ?)
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
            cursor.execute("DELETE FROM character WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error removing character: {e}")
        finally:
            conn.close()