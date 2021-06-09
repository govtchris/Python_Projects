

#import sqlite3 module
import sqlite3

#connecting to the database
conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')

#create the table if it doesn't already exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                Name TEXT, Species TEXT, IQ TEXT)")
    conn.commit
conn.close

#reconnecting to the database after seeing if the table has been created
conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')

rosterValues = (("Jean-Baptiste Zorg", "Human", "122"),\
                ("Korben Dallas", "Meat Popsicle", "100"),\
                ("Ak'not", "Mangalore", "-5"))

with conn:
    cur = conn.cursor()
    cur.executemany("INSERT INTO Roster(Name, Species, IQ) VALUES(?, ?, ?)", rosterValues)
    
