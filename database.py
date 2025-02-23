# database.py
import sqlite3

DATABASE_FILE = "ascender_path.db"  # Define the database file name

def create_tables():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            level INTEGER DEFAULT 1
        )
    """)

    # Create Stats table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            level INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0,
            xp_to_next_level INTEGER DEFAULT 100,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    """)

    # Create Quests table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Quests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            quest_type TEXT,
            stat_name TEXT,
            xp_reward INTEGER
        )
    """)


    conn.commit()
    conn.close()

def create_user_and_stats(username, str):
    """Creates a new user in the Users table and initializes their six stats in the Stats table"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    try:
        # 1 insert the new user into the users table
        cursor.execute("INSERT INTO Users (username) VALUES (?)", (username,))
        user_id = cursor.lastrowid

        # 2 define the six stats names
        stat_names = ["Career", "Learning", "Nutrition", "Relationship", "Spirituality", "Strength"]

        # 3 insert six stats recors for the new user, one for each stat name
        for stat_name in stat_names:
            cursor.execute("INSERT INTO Stats (user_id, name) VALUES(?, ?)", (user_id, stat_name))
            conn.commit()
            return user_id
        
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Database Error during user creation: {e}")
        return None
    
    finally:
        conn.close()


if __name__ == "__main__": # This block will run when you execute database.py directly
    create_tables()
    print("Database tables created (or already exist).")