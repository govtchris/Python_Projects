
#creating a class for mammals
class mammal:
    #using a dunder to let me attach arguments 
    def __init__(self, cName, heatGenerate):
        self.cName = cName
        self.heatGenerate = heatGenerate

    #Creating a print function to let me check to see if the dunder worked
    def myFunction(self):
        print("Hi, I am a " + self.cName + " and I am " + self.heatGenerate)

m1 = mammal("Dog", "endothermic")
m1.myFunction()
    
#creating a dog class from the mammal parent class
class dog(mammal):
    diet = "omnivore"
    title = "Man's Best Friend"

#creating a bird class from the parent mammal class
class bird(mammal):
    fur = "Feathers, not fur"
    
