import sqlite3


# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")

new_con = sqlite3.connect("tutorial.db")
cur = new_con.cursor()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
new_con.commit()  # Remember to commit the transaction after executing INSERT.
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")