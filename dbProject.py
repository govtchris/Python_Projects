
#import sqlit3 module
import sqlite3

#connecting to the test database create for these projects
conn = sqlite3.connect('test.db')

#create the table if it doesn't already exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Test ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        document TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
               
#making the required file list into a tuple                       
fileList = ('information.docx', 'Hello.txt', 'myImag.png', 
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg'
            )

#looping through the list to select only the files with .txt extensions
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Test (document) VALUES (?)", (x,))
            print(x)
conn.close()
