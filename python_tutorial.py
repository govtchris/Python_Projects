#
# Python: 3.9.5
#
# Chris Windsor
#
# Purpose: The Tech Academy Python Course
#          Demonstrating how to pass variables from function to 
#          while producing a functional game.  
#




def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)



def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name,l_name,age,gender))










if __name__ == "__main__":
    start()
