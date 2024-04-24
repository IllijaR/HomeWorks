import re
import sqlite3


class LogDataBase:
    def __init__(self, db_name='logins.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.c = self.conn.cursor()
        self.setup_table()

    def setup_table(self):
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')

    @staticmethod
    def check_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def check_password(password):
        return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d@])", password)

    @staticmethod
    def check_login(login):
        return re.match(r"^[a-zA-Z0-9_]+$", login)

    def register_or_update_user(self, login, email, password):
        if not self.check_email(email) or not self.check_password(password) or not self.check_login(login):
            return False
        self.c.execute('SELECT id FROM logins WHERE login=? OR email=?', (login, email))
        user_id = self.c.fetchone()
        if user_id:
            self.c.execute('UPDATE logins SET login=?, email=?, password=? WHERE id=?',
                           (login, email, password, user_id[0]))
        else:
            self.c.execute('INSERT INTO logins (login, email, password) VALUES (?, ?, ?)', (login, email, password))
        self.conn.commit()
        return True

    def login_user(self, login, password):
        self.c.execute('SELECT * FROM logins WHERE login=? AND password=?', (login, password))
        if self.c.fetchone():
            return True
        else:
            return False

    def close_connection(self):
        self.conn.close()
