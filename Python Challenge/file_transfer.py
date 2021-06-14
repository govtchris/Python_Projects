import shutil
import os

#set where the source of the files are located
source = "/Users/chriswindsor/Desktop/folderA/"

#set the destination path to FolderB
destination ="/Users/chriswindsor/Desktop/folderB/"
files = os.listdir(source)


for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

