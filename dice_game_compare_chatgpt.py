#-------------------------------------------------------------------------------

import random

def roll_dices(func):  #The roll_dices function generates 3 dice rolls for the given function func.
    a1 = func(1)       #func ist eine variable (Platzhalter) für die folgende Funktion my_function
    a2 = func(1)       #my_function wird mit dem Wert 1 ausgeführt
    a3 = func(1)
    return [a1, a2, a3]

def my_function(x):    #The my_function and enemy_function functions generate dice values, and are passed as arguments to the roll_dices function.
  return x * random.randint(1,20)

attack = roll_dices(my_function)
print("Your dices: {} + {} + {}".format(*attack))

def enemy_function(x):
  return x * random.randint(1,20)

defend = roll_dices(enemy_function)
print("Enemy dices: {} + {} + {}".format(*defend))

x = sum(1 for a, b in zip(attack, defend) if a > b)   #The zip function is used to compare elements of the attack and defend lists
y = sum(1 for a, b in zip(attack, defend) if a <= b)  #The sum function is used to count the number of wins and losses.

if x > y:
    print("Attacker win")
else:
    print("Attacker lose")
