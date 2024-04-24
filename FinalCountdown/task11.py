import re
import sqlite3

conn = sqlite3.connect('logins.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS logins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')


def check_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def check_password(password):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d@])", password)


def check_login(login):
    return re.match(r"^[a-zA-Z0-9_]+$", login)


def register_user(login, email, password):
    if not check_email(email) or not check_password(password) or not check_login(login):
        print("Ерорр")
        return False
    c.execute('SELECT id FROM logins WHERE login=? OR email=?', (login, email))
    user_id = c.fetchone()
    if user_id:
        c.execute('UPDATE logins SET login=?, email=?, password=? WHERE id=?', (login, email, password, user_id[0]))
    else:
        c.execute('INSERT INTO logins (login, email, password) VALUES (?, ?, ?)', (login, email, password))
    conn.commit()
    print("Данные юзера зарегано!")
    return True


def login_user(login, password):
    c.execute('SELECT * FROM logins WHERE login=? AND password=?', (login, password))
    if c.fetchone():
        print("Ви вошли!")
    else:
        print("Неправильный логин/пароль.")


register_user('boba', 'user@raid.com', 'haMe1!')
register_user('biba', 'user2@mail.com', 'Pass1!3')
register_user('23ger', 'user@google.com', 'haMe1!')

login_user('boba', 'haMe1!')

conn.close()
