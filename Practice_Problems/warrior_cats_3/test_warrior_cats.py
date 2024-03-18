from cat import Cat
from warrior_cat import WarriorCat
from clan import Clan
"""
########################################################################################################################
This File is used to test your code. I want you to make this file work when you click run!

You should play around with your code and add your own tests down bellow once you are done with the project!
########################################################################################################################
"""

# create a cat (kittypet)
hobbs = Cat("Hobbes", 16, "orange")
print(hobbs)
hobbs.speak()
hobbs.purr()

# create a warrior cat
TigerCrown = WarriorCat("Hobbes", 16, "orange", "Tigercrown")
print(TigerCrown)
TigerCrown.speak()
TigerCrown.purr()

# create a clan
ThunderClan = Clan("ThunderClan", "On a Hill")
print(ThunderClan)

# add a Warrior cat to teh clan
ThunderClan.addWarrior(TigerCrown)
print(ThunderClan.members())
print(TigerCrown.clan)

# promote the warrior cat the leader
ThunderClan.promoteLeader(TigerCrown)
print(ThunderClan.leader)

# create and add another cat the clan
w1 = WarriorCat("Steve", 2, "Black", "BrokenTail")
ThunderClan.addWarrior(w1)
print(ThunderClan.members())
print(w1.clan)

# TODO: Add your own tests down here