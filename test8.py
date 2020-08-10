
import sqlite3

conn=sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    our.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    our.execute("INSERT INTO tbl_persons(col_fname, col_lname,col_email) VALUES (?,?,?)", \
                ('Bob','Smith','bsmith@gmail.com'))
    conn.commit()
conn.close()
