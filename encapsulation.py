

##Creating a class that will be encapsulated

class protected:
    def __init__(self,number):
        #Creating a nurmal attribute
        self.a = 10
        #Creating a protected attribute
        self._b = 20
        #creating a private attribute
        self.__c = 30

protected = protected('number')
print(protected.a)
print(protected._b)
print(protected.__c)
