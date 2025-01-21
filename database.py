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
                    name TEXT NOT NULL
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
            cursor.execute("INSERT INTO characters (name) VALUES(?)", (character_data[0],))
            character_id = cursor.lastrowid # get the id of the new character
            stats = ['strength', 'agility', 'intelligence', 'endurance', 'perception']
            for stat in stats:
                cursor.execute("INSERT INTO character_stats (character_id, stat_name, xp) VALUES(?, ?, ?)", (character_id, stat, 0))
            conn.commit()
         except sqlite3.Error as e:
            print(f"Error adding character: {e}")
         finally:
            conn.close()

def get_all_characters():
    conn = create_connection()
    characters = {}
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT
                    characters.id,
                    characters.name,
                    character_stats.stat_name,
                    character_stats.xp
                FROM characters
                INNER JOIN character_stats
                ON characters.id = character_stats.character_id
                 ORDER BY characters.id, character_stats.stat_name
            """)
            rows = cursor.fetchall()
            for row in rows:
              character_id = row[0]
              character_name = row[1]
              stat_name = row[2]
              xp = row[3]

              if character_id in characters:
                  characters[character_id]["stats"].append({"stat_name": stat_name, "xp": xp})
              else:
                 characters[character_id] = {"id": character_id, "name": character_name, "stats": [{"stat_name": stat_name, "xp": xp}]}
        except sqlite3.Error as e:
            print(f"Error getting characters: {e}")
        finally:
            conn.close()
    return list(characters.values())

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

def create_character_stat_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS character_stats (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    character_id INTEGER NOT NULL,
                    stat_name TEXT NOT NULL,
                    xp INTEGER NOT NULL,
                    FOREIGN KEY (character_id) REFERENCES characters(id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error trying to create character stat table: {e}")
        finally:
            conn.close()