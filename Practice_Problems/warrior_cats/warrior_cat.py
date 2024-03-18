from cat import Cat

"""
########################################################################################################################
In this file you will define a WarriorCat 
This will use your Cat class so write this one 2nd
########################################################################################################################
"""

class WarriorCat(Cat):
    # create a WarriorCat class
    # A WarriorCat is a cat with a clan (starts empty but is set when added to a clan) and a warrior_name
    # Warrior Cat's do not meow, they speak, so overload speak() with a warrior cat greeting
    def __init__(self):
        super().__init__() # this class inherits the init from the Cat class on top of its own init
        pass  # replace with your code

    # str is used when printing a class
    def __str__(self):
        return ""  # replace this with a string representation of this class's info!

    def speak(self):
        # a warrior cat greeting includes warrior_name and clan (only if it is in one)
        pass  # print out what a warrior cat says
