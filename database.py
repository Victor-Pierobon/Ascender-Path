import sqlite3
from math import floor, sqrt, ceil

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("./ascender_path.db")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_quests_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quests(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           description TEXT NOT NULL,
                           rank TEXT NOT NULL
                           )
                    """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()


def add_quest(quest_name, quest_description, quest_rank):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO quests (name, description, rank) VALUES (?, ?, ?)", (quest_name, quest_description, quest_rank))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding quest: {e}")
        finally:
            conn.close()

def get_all_quests():
    conn = create_connection()
    quests = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, description, rank FROM quests")
            quests = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting quests: {e}")
        finally:
            conn.close()
    return quests

def remove_quest_from_db(quest_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quests WHERE id = ?", (quest_id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error removing quest: {e}")
        finally:
            conn.close()


def create_character_quests_table():
    conn= create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS character_quests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    character_id INTEGER NOT NULL,
                    quest_id INTEGER NOT NULL,
                    FOREIGN KEY (character_id) REFERENCES characters(id),
                    FOREIGN KEY (quest_id) REFERENCES quests(id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating character quests table: {e}")
        finally:
            conn.close()


def get_all_character_quests(character_id):
    conn = create_connection()
    quests = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                    SELECT
                        quests.id,
                        quests.name,
                        quests.description,
                        quests.rank
                    FROM quests
                    INNER JOIN character_quests
                    ON quests.id = character_quests.quest_id
                    WHERE character_quests.character_id = ?
                """, (character_id,))
            quests = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting all quests: {e}")
        finally:
            conn.close()
    return quests

def add_quest_to_character(character_id, quest_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO character_quests (character_id, quest_id)
                VALUES(?, ?)
            """, (character_id, quest_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding quest to character: {e}")
        finally:
            conn.close()

def complete_quest(character_id, quest_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM character_quests
                WHERE character_id = ? AND quest_id = ?
            """, (character_id, quest_id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error completing quest: {e}")
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
                cursor.execute("INSERT INTO character_stats (character_id, stat_name, xp, level) VALUES(?, ?, ?, ?)", (character_id, stat, 0, 0))
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
                    character_stats.xp,
                    character_stats.level
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
              level = row[4]

              if character_id in characters:
                  characters[character_id]["stats"].append({"stat_name": stat_name, "xp": xp, "level": level})
              else:
                 characters[character_id] = {"id": character_id, "name": character_name, "stats": [{"stat_name": stat_name, "xp": xp, "level": level}]}
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
                    level INTEGER NOT NULL,
                    FOREIGN KEY (character_id) REFERENCES characters(id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error trying to create character stat table: {e}")
        finally:
            conn.close()

def add_xp_to_stat(character_id, stat_name, xp_amount):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE character_stats
                SET xp = xp + ?
                WHERE character_id = ? AND stat_name = ?
            """, (xp_amount, character_id, stat_name,))
            conn.commit()
            update_character_stats(character_id)
        except sqlite3.Error as e:
            print(f"Error adding xp to stat: {e}")
        finally:
            conn.close()


def update_character_stats(character_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT  id, stat_name, xp, level FROM character_stats WHERE character_id = ?", (character_id,))
            character_stats = cursor.fetchall()

            character_level = 0
            for row in character_stats:
                stat_id = row[0]
                stat_name = row[1]
                xp = row[2]
                stat_level = row[3]

                xp_to_level_up = 5 + stat_level*(1.25 + stat_level/10)
                if xp >= floor(xp_to_level_up):
                 xp = xp - floor(xp_to_level_up)
                 stat_level = stat_level + 1
                 cursor.execute("UPDATE character_stats SET xp = ?, level = ? WHERE id = ?", (xp, stat_level, stat_id))
                character_level = character_level + stat_level

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating character stats: {e}")
        finally:
            conn.close()