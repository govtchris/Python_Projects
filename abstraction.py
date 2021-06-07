

from abc import ABC, abstractmethod

class car(ABC):
    #creating a regular method
    def driving(self, x):
        print("You drive a what?? ", x)
    # creating an abstract method and using a pass statement so it the data can be passed later.
    @abstractmethod
    def moving(self, x):
        pass

class truck(car):
    # Defining the payment method that was passed through
    def moving(self, x):
        print("You drive a big pickup", x)


obj = truck()
obj.driving("a Chevy")
obj.moving("truck!")
