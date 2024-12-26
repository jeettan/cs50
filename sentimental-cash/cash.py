# TODO

import cs50
import math

checker = 0
while (checker <= 0):
    checker = cs50.get_float("Change owed: ")

count = 0
tempcount = 0
x = checker

while (True):
    #First check

    if (x % 0.25 == 0):
        tempcount = x / 0.25
        count += tempcount
        break
    elif (x > 0.25):
        tempcount = math.floor(x / 0.25)
        x = round(x % 0.25, 2)
        count+= tempcount

    #Second check

    if (x % 0.1 == 0):
        tempcount = x / 0.1
        count += tempcount
        break
    elif (x > 0.1):
        tempcount = math.floor(x / 0.1)
        x = round(x % 0.1, 2)
        count += tempcount

    #Third check

    if (x % 0.05 == 0):
        tempcount = x / 0.05
        count += tempcount
        break
    elif (x > 0.05):
        tempcount = round(x / 0.1)
        x = round(x % 0.05, 2)
        count += tempcount

    #Remainder

    if (x % 0.01 == 0):
        tempcount = x / 0.01
        count += tempcount
        break
    elif (x > 0.01):
        x = x % 0.01
        tempcount = math.floor(x / 0.01)
        count += tempcount + 1
        break

print(round(count))