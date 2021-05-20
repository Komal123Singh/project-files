import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('create table report(
                id integer primary key autoincrement,
                name text,
                eng integer,
                maths integer,
                science integer,
                hindi integer,
                elective integer')
conn.commit()