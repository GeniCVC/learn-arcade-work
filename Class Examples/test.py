# Written by Matthew Jackson
# Imports random function
import random

# Introduction
print("Welcome to Starship Escape!")
print("You have stolen a starship from the Republic of Aros to make your way across the Tessa Galaxy.")
print("The Republic wants their starship back and are chasing after you! ")
print("Survive your trek across the galaxy and out run the Republic of Aros.")
# Variable to keep track of distance traveled
miles = 0

# Variable to keep track of warp-drive overheating
overheat = 0

# Variable to keep track of need of fuel
fuel = 0

# Variable to keep track of distance between Republic and Starship
republic = -20

# Variable to keep track of gas canister
can = 4

# Variable to check to see if starship finds resource cache.
cache = 20

# Sets done variable as false
done = False

# while loop to loop game.
while done == False:
    # Options
    print("A. Refuel Tank.")
    print("B. Go cruising speed.")
    print("C. Go warp speed.")
    print("D. Cool off the warp drive.")
    print("E. Status check. ")
    print("Q. Quit")

    # Choice input
    Choice = input("What is your choice? ")

    # A choice input
    if Choice == "a" or Choice == "A":
        if can <= 0:
            print("You are out of fuel in your canister")
        if can >= 1:
            print("You refuel your ship from your fuel canister")
            can -= 1
            fuel = 0

    # B choice input
    if Choice == "b" or Choice == "B":
        print("You move ahead at cruising speed.")
        # Rolls a random number between range
        my_number1 = random.randrange(5, 12)
        print("You traveled ", my_number1, " light-years.")
        miles += my_number1
        fuel += 1
        overheat += 1
        # Rolls a random number between range
        my_number = random.randrange(7, 14)
        republic = republic + my_number - my_number1
        # Rolls a random number between range
        my_number = random.randrange(1, 20)
        # Checks if my_number matches cache value
        if my_number == cache:
            print("You found a resource cache!")
            can = 3
            overheat = 0
            fuel = 0

    # C choice input
    if Choice == "c" or Choice == "C":
        print("You move ahead at warp speed.")
        # Rolls a random number between range
        my_number1 = random.randrange(14, 20)
        print("You traveled ", my_number1, " light-years.")
        miles += my_number1
        fuel += 1
        # Rolls a random number between range
        my_number = random.randrange(1, 3)
        overheat = my_number + overheat - my_number1
        # Rolls a random number between range
        my_number = random.randrange(7, 14)
        republic = my_number + republic - my_number1
        # Rolls a random number between range
        my_number = random.randrange(1, 20)
        # Checks if my_number matches cache value
        if my_number == cache:
            print("You found a resource cache!")
            can = 3
            overheat = 0
            fuel = 0

    # D choice input
    if Choice == "d" or Choice == "D":
        print("You cool down your warp drive.")
        # Rolls a random number between range
        my_number = random.randrange(7, 14)
        republic = republic + my_number
        overheat = 0

    # E choice input
    if Choice == "e" or Choice == "E":
        print("Light-years traveled : ", miles)
        print("Fuel in Canister : ", can)
        # Makes republic value into positive.
        behind = republic * -1
        print("The Republic is ", behind, " light-years behind you.")

    # Q choice input
    if Choice == "q" or Choice == "Q":
        print("You've decided to quit the game.")
        # Ends game
        done = True

    # Warning Screen
    if fuel == 4 and fuel != 6 and done != True:
        print("You are low on gas.")

    # Lose screen
    if fuel == 6 and done != True:
        print("You ran out of gas!")
        # Ends game
        done = True

    # Warning Screen
    if 5 <= overheat <= 7 and done != True:
        print("Your warp drive is starting to overheat.")

    # Lose screen
    if overheat >= 8 and done != True:
        print("Your warpdrive overheated and exploded!")
        # Ends game
        done = True

    # Warning Screen
    if -5 >= republic >= 0:
        print("The Republic is getting close!")

    # Lose screen
    if republic >= 0 and done != True:
        print("The Republic caught you!")
        # Ends game
        done = True

    # Win screen
    if miles >= 200 and done != True:
        print("You were able to lose the Republic. You won!")
        # Ends game
        done = True
