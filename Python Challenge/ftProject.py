import tkinter 
from tkinter import *
from tkinter import filedialog
import shutil
import os
import datetime as dt


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(481, 203))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')


        #Browse1 will search the directory and find the folder to check and pull from
        self.btnBrowse1 = Button(self.master, text='Browse...', font=('Helvetica', 10), width=13, height=2, bg='lightgrey', command=self.askDir1)
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(20,0), sticky=NE)

        #Label1 will show the file selection from the Browse1 button
        self.txtLabel1 = Label(self.master, text='', font=("Helvetica", 16), width=30)
        self.txtLabel1.grid(row=3, column=1, columnspan=12, padx=(30,0), pady=(20,0))

        #Browse2 will search the directory and find the folder to move files to
        self.btnBrowse2 = Button(self.master, text='Browse...', font=('Helvetica', 10), width=13, height=2, bg='lightgrey', command=self.askDir2)
        self.btnBrowse2.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=NE)

        #Label2 will show the file selection from the Browse2 button
        self.txtLabel2 = Label(self.master, text='', font=("Helvetica", 16), width=30)
        self.txtLabel2.grid(row=4, column=1, columnspan=12, padx=(30,0), pady=(10,0))

        #btnCheck will be call the function used to check the files to see if there has been any change in the last 24hrs and
        #and the transfer the files if there has been. 
        self.btnCheck = Button(self.master, text='Check for files...', font=('Helvetica', 10), width=13, height=3, bg='lightgrey', command=self.check)
        self.btnCheck.grid(row=5, column=0, padx=(30,0), pady=(10,30), sticky=NE)

        #button that will close the window
        self.btnClose = Button(self.master, text='Close Program', font=('Helvetica', 10), width=13, height=3, bg='lightgrey', command=self.close)
        self.btnClose.grid(row=5, column=12, padx=(30,0), pady=(10,30), sticky=NE)

        self.Label3 = Label(self.master, text='', font=("Helvetica", 16), width=30)
        self.Label3.grid(row=6, column=0, columnspan=12, padx=(30,0), pady=(10,30), sticky=NE)

        
    #functions for selecting a directory from the os and then displaying it in the proper area.
    def askDir1(self):
        x= tkinter.filedialog.askdirectory()
        self.txtLabel1.config(text=x +"/")
        #self.Label3.config(text=x)

    def askDir2(self):
        x= tkinter.filedialog.askdirectory()
        self.txtLabel2.config(text=x + "/")
        #self.Label3.config(text=x)

    def check(self):
        src = self.txtLabel1.cget("text")
        des = self.txtLabel2.cget("text")
        now = dt.datetime.now()
        ago = now-dt.timedelta(hours=24)
        self.Label3.config(text=src+ " " +des)
        files = os.listdir(src)
        for i in files:
            path = os.path.join(src, i)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime < ago:
                shutil.move(path, des) 

    #function for the close program button
    def close(self):
        self.master.destroy()
        

    

if __name__ == "__main__":
   root = Tk()
   App = ParentWindow(root)
   root.mainloop
