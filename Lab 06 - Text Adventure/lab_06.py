# House Class
class House:
    # Defining directions
    def __init__(self, description, north, east, south, west):
        self.description = description
        # North
        self.north = north
        # East
        self.east = east
        # South
        self.south = south
        # West
        self.west = west


# Main Function
def main():
    # Creates list for rooms
    room_list = []
    # Creates and sets next_room variable to 0
    next_room = 0
    # Creates and sets current_room variable to 0
    current_room = 0
    # Sets done variable to False
    done = False

    # Second Bedroom
    room = House("You are in the second bedroom, there is a door to the east.", None, 1, None, None)
    # Appends direction to room_list
    room_list.append(room)

    # South Hall
    room = House("You are in the south hall, you can go east, west, or north.", 4, 2, None, 0)
    # Appends direction to room_list
    room_list.append(room)

    # Dining Hall
    room = House("You are in the dining hall, you can go west", None, None, None, 1)
    # Appends direction to room_list
    room_list.append(room)

    # First Bedroom
    room = House("You are in the first bedroom, you can go east.", None, 4, None, None)
    # Appends direction to room_list
    room_list.append(room)

    # North Hall
    room = House("You are in the north hall , you can go east, west, north, or south.", 6, 5, 1, 3)
    # Appends direction to room_list
    room_list.append(room)

    # Kitchen
    room = House("You are in the kitchen, you can go west", None, None, None, 4)
    # Appends direction to room_list
    room_list.append(room)

    # Balcony
    room = House("You are on the balcony, you can south.", None, None, 4, None)
    # Appends direction to room_list
    room_list.append(room)

    #
    while not done:
        # Prints the current room information
        print(room_list[current_room].description)
        # Sets direction variable to input
        direction = input("Which way would you like to go (N - E - S - W) or enter Q to quit.").lower()

        # North Direction
        if direction[0] == 'N' or direction[0] == 'n':
            next_room = room_list[current_room].north

        # South Direction
        elif direction[0] == 'S' or direction[0] == 's':
            next_room = room_list[current_room].south

        # East Direction
        elif direction[0] == 'E' or direction[0] == 'e':
            next_room = room_list[current_room].east

        # West Direction
        elif direction[0] == 'W' or direction[0] == 'w':
            next_room = room_list[current_room].west

        # Quit Option
        elif direction[0] == 'Q' or direction[0] == 'q':
            # Prints Quit Confirmation
            print("You decided to quit the game.")
            # Sets done to True and ends program.
            done = True

        # If input is not valid option
        else:
            print("Please enter a valid direction.")
            # Continues Program
            continue

        # If input is not a valid direction
        if next_room is None and done != True:
            print("You cannot go that way.")
            # Continues Program
            continue

        #
        current_room = next_room


# Ends main function
main()
