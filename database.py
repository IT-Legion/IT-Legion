import sqlite3

class Database:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS person (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        dob DATE NOT NULL,
                        email TEXT NOT NULL,
                        phone_mobile TEXT
                    )'''
        self.conn.execute(query)
        self.conn.commit()

    def insert_person(self, first_name, last_name, dob, email, phone_mobile):
        query = '''INSERT INTO person (first_name, last_name, dob, email, phone_mobile) 
                   VALUES (?, ?, ?, ?, ?)'''
        self.conn.execute(query, (first_name, last_name, dob, email, phone_mobile))
        self.conn.commit()

    def close(self):
        self.conn.close()
