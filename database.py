import sqlite3

class Database:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        create_user_table = '''CREATE TABLE IF NOT EXISTS user (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL,
                                    password TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    phone_mobile TEXT
                                )'''

        create_person_table = '''CREATE TABLE IF NOT EXISTS person (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    first_name TEXT NOT NULL,
                                    last_name TEXT NOT NULL,
                                    dob DATE NOT NULL,
                                    email TEXT NOT NULL,
                                    phone_mobile TEXT
                                )'''
        
        

        self.conn.execute(create_person_table)
        self.conn.execute(create_user_table)
        self.conn.commit()

    def insert_person(self, first_name, last_name, dob, email, phone_mobile):
        query = '''INSERT INTO person (first_name, last_name, dob, email, phone_mobile) 
                   VALUES (?, ?, ?, ?, ?)'''
        self.conn.execute(query, (first_name, last_name, dob, email, phone_mobile))
        self.conn.commit()

    def insert_user(self, username, password, email, phone_mobile):
        query = '''INSERT INTO user (username, password, email, phone_mobile) 
                   VALUES (?, ?, ?, ?)'''
        self.conn.execute(query, (username, password, email, phone_mobile))
        self.conn.commit()

    def user_exists(self, username):
        query = '''SELECT * FROM user WHERE username = ?'''
        result = self.conn.execute(query, (username,))
        return result.fetchone() is not None

    def email_exists(self, email):
        query = '''SELECT * FROM user WHERE email = ?'''
        result = self.conn.execute(query, (email,))
        return result.fetchone() is not None

    def phone_mobile_exists(self, phone_mobile):
        query = '''SELECT * FROM user WHERE phone_mobile = ?'''
        result = self.conn.execute(query, (phone_mobile,))
        return result.fetchone() is not None

    def close(self):
        self.conn.close()
