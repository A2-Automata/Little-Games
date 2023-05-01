#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Learning
# Author:      Rupp
# Created:     21.06.2022
#-------------------------------------------------------------------------------

# Python Program to triple dice game

# Program to generate a random number between 1 and 20

# importing the random module
import random

def my_function(x):
  return x * random.randint(1,20)

a1 = my_function(1)
a2 = my_function(1)
a3 = my_function(1)
a = "Your dices: {0} + {1} + {2}".format(a1,a2,a3)
print(a)

def enemy_function(x):
  return x * random.randint(1,20)

b1 = my_function(1)
b2 = my_function(1)
b3 = my_function(1)
b = "Enemy dices: {0} + {1} + {2}".format(b1,b2,b3)
print(b)

# Vergleich der Würfelpaare
attack = [int(a1), int(a2), int(a3)]
defend = [int(b1), int(b2), int(b3)]
x = 0
y = 0
#Vergleichen von Listenelementen mit for Schleife (Delft Stack)

for i in attack:
    for j in defend:
        if(attack.index(i) == defend.index(j) and i > j):
            #print("a =", a)
            x += 1
        elif(attack.index(i) == defend.index(j) and i <= j):
            #print("b =", b)
            y += 1
        else:
            None

if(x > y):
    print("Attacker win")
else:
    print("Attacker lose")