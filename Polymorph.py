

#Parent class mtg card
class mtgCard:
    name = "swords to plowshares" 
    cmc = 1
    color = "White"

    #Creating a method to differentiate between two similar cards.
    #This took me a bit to figure out because the cmc input was a string not an integer!
    def mtgCardInfo(self):
        card_Name = input("Please input the name of your card: \n>>>")
        card_Name = card_Name.lower()
        card_CMC = int(input("Please input the cards mana value: \n>>>"))
        card_Color = input("Please input the color identity: \n>>>")
        if (card_Name == self.name and card_CMC == self.cmc and card_Color == self.color):
            print("Opponent gains life equal to the creatures power.")
        elif (card_Name == "path to exile" and card_CMC == self.cmc):
            print("Opponent fetches a basic land for the field.")
        else:
            print("You Lose")
           
    
    
#Child class for a blue control card
class blue(mtgCard):
    name = "Stasis"
    cmc = 2
    color = "Blue"
    saltlvl = 10
    purpose = "control"

    #Creating a method to figure out if the person
    def mtgCardInfo(self):
        play_Style = input("Please type Ramp, Control, or Aggro: \n>>>")
        #Added this to help make in case there was an issue with case sensitivity 
        play_Style = play_Style.lower()
        salt_LVL = int(input("Please input how salty you want to make you opponents feel with 10 being the highest level: \n>>>"))
        if (play_Style == self.purpose and salt_LVL >= 8):
            print("Do ya thang, ya jerk.")
        else:
            print("Play something else")
            
   
    

#Child class for a green ramp card 
class green(mtgCard):
    name = "Cultivate"
    cmc = 3
    color = "Green"
    popularity = 3
    ramp = "1 extra land"


    def mtgCardInfo(self):
        easy = input("Do you like to have fun or play on easy mode? \nType Yes or No>>>")
        easy = easy.lower()
        if (easy == "yes"):
            print("Put the following card in every deck you want! " + green.name)
        else:
            print("No harm no foul!")
                                                                            
                        

if __name__ == '__main__':

  
    cardinfo = mtgCard()
    cardinfo.mtgCardInfo()
    
    control = blue()
    control.mtgCardInfo()
    
    ramp = green()
    ramp.mtgCardInfo()

    
