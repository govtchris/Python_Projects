
#this variable is global
name = 'Python'

def getName():
    #this variable is local to the getName() function
    name = "Smeeve"
    print("I am coding with {}".format(name))


getName()
