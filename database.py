# Import Python's SQLite library
import sqlite3

# Name of file where data will be stored
DATABASE = "habits.db"

# Open a connection to the database and return it
def get_connection():
    # Connect to the database file
    conn = sqlite3.connect(DATABASE)
    #Lets us access columns by name, like row["name"], instead of row[1]\
    conn.row_factory = sqlite3.Row
    # Turn on foreign key rules
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Create tables if they don't already exist
def init_db():
    # Open a connection to the databse
    conn = get_connection()

    #Create habits table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            -- Unique number for each habit, assigned automatically
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            -- The habit's name; required, and no two habits can share a name
            name TEXT NOT NULL UNIQUE,
            -- The data the habit was created, stoed as a text like 2026-11-08
            created_at TEXT NOT NULL
        )
    """)

    #Create the checkins table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS checkins (
            -- Unique number for each check-in
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            -- Which habit this check-in belongs to; deleting the habit deletes its check-ins
            habit_id INTEGER NOT NULL REFERENCES habits(id) ON DELETE CASCADE,
            -- The day the habit was completed
            date TEXT NOT NULL,
            -- Prevent checking off the same habit twice on the same day
            UNIQUE(habit_id, date)
        )
    """)

    # Save changes to database file
    conn.commit()
    #Close the connection to free it
    conn.close()

# Only run this when the file is run directly
if __name__ == "__main__":
    #Create tables
    init_db()
    #Confirmation
    print("Database Initialized")