import sqlite3

DATABASE_NAME = "ascender_path.db"

def create_connection():
    """Creates a database connection to ascender_path.db."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tasks_table():
    """Creates the tasks table if it dosen't exist."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

def add_task_to_db(description):
    """Adds a new task to the database."""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding task to database: {e}")
        finally:
            conn.close()

def get_tasks_from_db():
    """Retrieves all tasks from the database."""
    conn = create_connection()
    tasks = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, description FROM tasks")
            rows =cursor.fetchall()
            for row in rows:
                tasks.append({"id": row[0], "description": row[1]})
        except sqlite3.Error as e:
            print(f"Error getting tasks from database: {e}")
        finally:
            conn.close()
    return tasks


def delete_tasks_from_db(task_id):
    """Deletes a task from the db by its ID"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id))
            conn.commit()

        except sqlite3.Error as e:
            print(f"Error deleting task from database: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    create_tasks_table()
    tasks = get_tasks_from_db()
    print("Tasks in database:")
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}")
