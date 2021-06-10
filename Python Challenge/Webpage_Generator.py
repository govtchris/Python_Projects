
import webbrowser
from tkinter import *

f = open("staytuned.html","w")
message = """
<html>
<body>
<h1>Stay tuned for our amazing summer sale!</h1>
</body>
</html>"""
f.write(message)
f.close()

filename = ("file:///Users/chriswindsor/Desktop/Python_Projects/Python Challenge/staytuned.html")
webbrowser.open_new_tab(filename)


