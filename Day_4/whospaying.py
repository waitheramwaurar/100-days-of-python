#Chooses from a list of people,who pays for the whole meal
#The list is taken as input of comma separated names, there is a space after the comma

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

chosen_one = random.randint(0, len(names)-1)
print(f"{names[chosen_one]} is going to buy the meal today.")