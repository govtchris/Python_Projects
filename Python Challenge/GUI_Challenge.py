
import tkinter 
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(481, 203))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        #set variables for the input fields in case I ever want to use the entered text
        self.input1 = StringVar()
        self.input2 = StringVar()

        #This will display the directory entered from the askDir() function
        self.lblDir = Label(self.master, text='', font=('Helvetica', 16), fg='black', bg='lightgrey' )
        self.lblDir.grid(row=0, rowspan=1, column=0, columnspan=12,  padx=(30,0), pady=(10,0), sticky=NE)

        #Browse button 1 will take the text from input1 if there is a call for it
        self.btnBrowse1 = Button(self.master, text='Browse...', font=('Helvetica', 10), width=13, height=2, bg='lightgrey')
        self.btnBrowse1.grid(row=3, column=0, padx=(30,0), pady=(20,0), sticky=NE)

        #input1
        self.txtInput1 = Entry(self.master,text=self.input1, font=("Helvetica", 16), width=30 )
        self.txtInput1.grid(row=3, column=1, columnspan=12, padx=(30,0), pady=(20,0))

        #Browse button 2 that will take text from input2 
        self.btnBrowse2 = Button(self.master, text='Browse...', font=('Helvetica', 10), width=13, height=2, bg='lightgrey')
        self.btnBrowse2.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=NE)

        #input2
        self.txtInput2 = Entry(self.master, text=self.input2, font=("Helvetica", 16), width=30)
        self.txtInput2.grid(row=4, column=1, columnspan=12, padx=(30,0), pady=(10,0))

        #Button for looking for files in the directory 
        self.btnCheck = Button(self.master, text='Check for files...', font=('Helvetica', 10), width=13, height=3, bg='lightgrey', command=self.askDir)
        self.btnCheck.grid(row=5, column=0, padx=(30,0), pady=(10,30), sticky=NE)

        #button that will close the window
        self.btnClose = Button(self.master, text='Close Program', font=('Helvetica', 10), width=13, height=3, bg='lightgrey', command=self.close)
        self.btnClose.grid(row=5, column=12, padx=(30,0), pady=(10,30), sticky=NE)

        
    #function for selecting a directory from the os and then displaying it
    def askDir(self):
        x= tkinter.filedialog.askdirectory()
        self.lblDir.config(text=x)


    #function for the close program button
    def close(self):
        self.master.destroy()
        

    

if __name__ == "__main__":
   root = Tk()
   App = ParentWindow(root)
   root.mainloop
