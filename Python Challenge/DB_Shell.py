Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/chriswindsor/Desktop/Python_Projects/Python Challenge/DB_Challenge.py
>>> 
= RESTART: /Users/chriswindsor/Desktop/Python_Projects/Python Challenge/DB_Challenge.py
Traceback (most recent call last):
  File "/Users/chriswindsor/Desktop/Python_Projects/Python Challenge/DB_Challenge.py", line 27, in <module>
    cur.executemany("INSERT INTO Roster(Name, Species, IQ) VALUES(?, ?, ?)", rosterValues)
sqlite3.OperationalError: database is locked
>>> 
= RESTART: /Users/chriswindsor/Desktop/Python_Projects/Python Challenge/DB_Challenge.py
>>> c.execute("UPDATE Roster SET Species=? WHERE Name=?",
	  ("Korben Dallas", "Human"))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c.execute("UPDATE Roster SET Species=? WHERE Name=?",
NameError: name 'c' is not defined
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=?",
	  ("Korben Dallas", "Human"))
<sqlite3.Cursor object at 0x7fbf946efc70>
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? and IQ=?",
	  ("Korben Dallas", "Human"))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? and IQ=?",
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 3, and there are 2 supplied.
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ("Korben Dallas", "Human"))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 3, and there are 2 supplied.
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ("Korben Dallas", "Human", "100"))
<sqlite3.Cursor object at 0x7fbf946efc70>
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ("Human", "Korben Dallas", "100"))
<sqlite3.Cursor object at 0x7fbf946efc70>
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Human', 'Korben Dallas', '100'))
<sqlite3.Cursor object at 0x7fbf946efc70>
>>> with conn:
	cur = conn.cursor()
	cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Human', 'Korben Dallas', '100'))

	
<sqlite3.Cursor object at 0x7fbf941fc0a0>
>>> 
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Human', 'Korben Dallas', '100'))
    cur = conn.cursor()
    
<sqlite3.Cursor object at 0x7fbf941fc0a0>
>>> cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Human', 'Korben Dallas', '100'))
    conn.commit
    
<sqlite3.Cursor object at 0x7fbf941fc0a0>
>>>  cur.execute("SELECT Name, WHERE Species == Human")
 
SyntaxError: unexpected indent
>>> cur.execute("SELECT Name, WHERE Species == Human")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    cur.execute("SELECT Name, WHERE Species == Human")
sqlite3.OperationalError: near "WHERE": syntax error
>>> cur.execute("SELECT Name FROM Roster WHERE Species == Human")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cur.execute("SELECT Name FROM Roster WHERE Species == Human")
sqlite3.OperationalError: no such column: Human
>>> cur.execute("SELECT Name FROM Roster WHERE Species == "Human"")
SyntaxError: invalid syntax
>>> cur.execute("SELECT Name FROM Roster WHERE Species == 'Human' ")
<sqlite3.Cursor object at 0x7fbf941fc0a0>
>>> with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")

    
<sqlite3.Cursor object at 0x7fbf941fc110>
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
>>> with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")

    
<sqlite3.Cursor object at 0x7fbf941fc180>
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")
    
>>> 
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")
    
>>> with conn:
    cur = conn.cursor()
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Buman', 'Korben Dallas', '100'))
    conn.commit

    
<sqlite3.Cursor object at 0x7fbf941eff80>
<built-in method commit of sqlite3.Connection object at 0x7fbf946cc6c0>
>>> with conn:
    cur = conn.cursor()
    cur.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
	  ('Human', 'Korben Dallas', '100'))
    conn.commit

    
<sqlite3.Cursor object at 0x7fbf946efc70>
<built-in method commit of sqlite3.Connection object at 0x7fbf946cc6c0>
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")
    
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")
    for row in cur.fetchall():
	    
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == 'Human'")
    for row in cur.fetchall():
	    print (row)
	    
>>> 
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name FROM Roster WHERE Species == Human")
    for row in cur.fetchall():
	    print (row)
	    
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species == Human")
    for row in cur.fetchall():
	    print (row)
	    
>>> conn = sqlite3.connect('/Users/chriswindsor/Desktop/Python_Projects/test_database.db')
    with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
	    print (row)
	    
>>> 
= RESTART: /Users/chriswindsor/Desktop/Python_Projects/Python Challenge/DB_Challenge.py
('Jean-Baptiste Zorg', '122')
('Korben Dallas', '100')
>>>  with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
	    print (row)
	    
SyntaxError: unexpected indent
>>> with conn:
    cur = conn.cursor()
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
	    print (row)

	    
<sqlite3.Cursor object at 0x7ff521cf2ce0>
('Jean-Baptiste Zorg', '122')
('Korben Dallas', '100')
>>> 