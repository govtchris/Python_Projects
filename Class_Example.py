
#creating a class for mammals
class mammal:
    def __init__(self, cName, heatGenerate):
        self.cName = cName
        self.heatGenerate = heatGenerate

    def myFunction(self):
        print("Hi, I am a " + self.cName + " and I am " + self.heatGenerate)

m1 = mammal("Dog", "endothermic")
m1.myFunction()
    
    
class dog(mammal):
    diet = "omnivore"
    title = "Man's Best Friend"

class bird(mammal):
    fur = "Feathers, not fur"
    
