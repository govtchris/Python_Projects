
import webbrowser
from tkinter import *


class ParentWindow(Frame):

    #creating the GUI    
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(481, 203))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        
         #Browse button 1 will take the text from input1 if there is a call for it
        self.btnBrowse1 = Button(self.master, text='Submit...', font=('Helvetica', 10),\
        width=13, height=2, bg='lightgrey', command= self.webOpen)
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(20,0), sticky=NE)

        #input1
        self.txtInput1 = Entry(self.master,text=StringVar(), font=("Helvetica", 16), width=30 )
        self.txtInput1.grid(row=3, column=1, columnspan=12, padx=(30,0), pady=(20,0))


    #function that creates a webpage using the input from the GUI
    def webOpen(self):

        txt = self.txtInput1.get()
        f = open("staytuned.html","w")
        message =( """
        <html>
        <body>
        <h1>
        {}
        </h1>
        </body>
        </html>""".format(txt))
        f.write(message)
        f.close()
        
        filename = ("file:///Users/chriswindsor/Desktop/Python_Projects/Python Challenge/staytuned.html")
        webbrowser.open_new_tab(filename)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop
