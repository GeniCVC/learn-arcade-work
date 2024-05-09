# King Solomon's Treasure
# By Matthew Jackson

# Notes on wanted additions
# Wanted to add enemies, more rooms, and different room events
# Had idea for multiple treasure rooms with different Proverbs,
# and after getting all the treasure having to escape in a certain amount of moves.
# Tried to put rooms in text file and reading it, but had a few difficulties. May try it again in the future.

# Random Library
import random


class Directions:
    # Defining directions, items, and traps
    def __init__(self, description, items, n, ne, nw, e, s, se, sw, w, up, down, trap_chance, riddle=None,
                 is_treasure_room=False):
        self.description = description
        self.items = items  # List of items in the room
        # Directions
        self.n = n
        self.ne = ne
        self.nw = nw
        self.e = e
        self.s = s
        self.se = se
        self.sw = sw
        self.w = w
        self.up = up
        self.down = down
        # Trap chance
        self.trap_chance = trap_chance
        # Treasure room
        self.is_treasure_room = is_treasure_room
        # Riddle
        self.riddle = riddle

    # Method to enter a room and check for traps
    def enter(self, player, safe_action=False):
        print(self.description)
        if not safe_action and random.random() < self.trap_chance:
            print("You triggered a trap!")
            player.health -= random.randint(5, 20)
            if player.health <= 0:
                print("You succumbed to the trap. Game Over!")
                exit()
        if self.is_treasure_room:
            print("Congratulations! You found the treasure room!")
            print("To unlock the treasure, you must solve the riddle.")
            if self.riddle:
                print("Riddle:", self.riddle)

        # Check if there are items in the room
        if self.items:
            print("You see some items in the room:", ", ".join(self.items))

    # Method to display available directions and items
    def available_actions(self):
        actions = []
        if self.items:
            actions.append("Pick up items")
        if self.n is not None:
            actions.append(("Go north", self.n))
        if self.ne is not None:
            actions.append(("Go northeast", self.ne))
        if self.nw is not None:
            actions.append(("Go northwest", self.nw))
        if self.e is not None:
            actions.append(("Go east", self.e))
        if self.s is not None:
            actions.append(("Go south", self.s))
        if self.se is not None:
            actions.append(("Go southeast", self.se))
        if self.sw is not None:
            actions.append(("Go southwest", self.sw))
        if self.w is not None:
            actions.append(("Go west", self.w))
        if self.up is not None:
            actions.append(("Go up", self.up))
        if self.down is not None:
            actions.append(("Go down", self.down))
        # Check if the room is the treasure room
        if self.is_treasure_room:
            actions.append("Solve riddle")
        actions.append("Check health")
        return actions


# Player Class
class Player:
    def __init__(self, health):
        self.health = health
        self.inventory = []  # Player's inventory
        self.last_action_safe = False  # Track if the last action was safe from traps

    # Method to pick up items
    def pick_up_item(self, room):
        if room.items:
            self.inventory.extend(room.items)
            room.items = []  # Remove items from the room
            print("You picked up the items.")
        self.last_action_safe = True  # Update last action as safe

    # Method to open inventory and use items
    def open_inventory(self):
        print("Inventory:")
        if self.inventory:
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")
            choice = input("Enter the number of the item you want to use, or 'cancel' to go back: ")
            if choice.lower() == 'cancel':
                return
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(self.inventory):
                    item = self.inventory.pop(choice_index)
                    print(f"You used {item}.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Invalid input.")
        else:
            print("Your inventory is empty.")
        self.last_action_safe = True  # Update last action as safe

    # Method to use bandages and heal
    def use_bandages(self):
        if 'Bandages' in self.inventory:
            # Healing logic
            heal_amount = random.randint(10, 30)
            self.health = min(100, self.health + heal_amount)
            print(f"You used bandages and healed for {heal_amount} health.")
            # Remove bandages from inventory
            self.inventory.remove('Bandages')
            self.last_action_safe = True  # Update last action as safe
        else:
            print("You don't have any bandages to use.")
            self.last_action_safe = True  # Update last action as safe

    # Method to check player's health
    def check_health(self):
        print(f"Your current health is {self.health}.")
        self.last_action_safe = True  # Update last action as safe


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

    print("You are a treasure hunter who has heard talk of the ancient treasure of King Solomon. You have traveled to "
          "the entrance of his tomb. Through the use of proverbs you may be able to find it, but be on the lookout "
          "for traps...")

    # Entrance
    room = Directions("You are at the entrance of the tomb of King Solomon", [], 1, None, None, None,
                      None, None, None, None, None, None, trap_chance=0)
    room_list.append(room)

    # First room
    room = Directions("You enter a dimly lit room with hieroglyphs on the walls.", ["Bandages"], None, 5, None, 7,
                      None, None, None, 2, None, None, trap_chance=0.5)
    print("After entering the room, the door behind you closes, and you are left with no way out.")
    room_list.append(room)

    # Second room
    room = Directions(
        "You find yourself in a narrow corridor with strange symbols etched into the floor.",
        [], None, 6, None, 8, None, None, None, 1, None, None, trap_chance=0.3)
    room_list.append(room)

    # Third room
    room = Directions(
        "You step into a hall lined with ancient statues, their eyes seeming to follow your every move.",
        ["Bandages"], 1, 7, None, 9, None, None, None, 2, None, None, trap_chance=0.4)
    room_list.append(room)

    # Fourth room
    room = Directions(
        "You find yourself in a grand dining hall, the table still set as if waiting for guests.",
        [], None, 8, None, None, None, None, None, 3, None, None, trap_chance=0)
    room_list.append(room)

    # Fifth room
    room = Directions("You enter a small chamber with a stone bed and a faded tapestry.", [], 2, None,
                      None, None, None, None, None, None, None, None, trap_chance=0)
    room_list.append(room)

    # Sixth room
    room = Directions("You find yourself in a narrow hallway with torches flickering ominously.",
                      [], None, None, None, 10, 2, None, None, None, None, None, trap_chance=0.7)
    room_list.append(room)

    # Seventh room
    room = Directions(
        "You step into a musty kitchen with pots and pans still hanging from the walls.",
        ["Bandages"], 3, 11, None, None, None, None, None, 6, None, None, trap_chance=0.4)
    room_list.append(room)

    # Eighth room
    room = Directions("You emerge onto a balcony overlooking a vast cavern below.", [], None, None,
                      None, None, 4, None, None, 7, None, None, trap_chance=0.8)
    room_list.append(room)

    # Ninth room
    room = Directions(
        "You find yourself back in the hall with the statues, but this time a sense of dread fills the air.",
        [], 5, None, None, 12, None, None, None, 8, None, None, trap_chance=0.4)
    room_list.append(room)

    # Tenth room
    room = Directions(
        "You enter a dimly lit passage with strange noises echoing from the darkness.", [],
        None, None, None, 11, None, None, None, 6, 12, None, trap_chance=0.6)
    room_list.append(room)

    # Eleventh room
    room = Directions("You find yourself at a dead end, the walls closing in around you.", [], 7,
                      None, None, None, None, None, None, None, None, None, trap_chance=0.8)
    room_list.append(room)

    # Treasure Room
    room = Directions(
        "You've found the treasure room! But to unlock the treasure, you must solve the riddle.",
        [], None, None, None, None, None, None, None, None, None, 10, trap_chance=0, is_treasure_room=True,
        riddle="The fear of the LORD is the beginning of wisdom, and the knowledge of the Holy One is _____________.")
    room_list.append(room)

    # Player's Health
    player = Player(100)

    # While Loop
    while not done:
        # Enter the current room and check for traps
        room_list[current_room].enter(player, safe_action=player.last_action_safe)

        # Display available actions
        print("Available Actions:")
        actions = room_list[current_room].available_actions()
        for action in actions:
            if isinstance(action, tuple):
                print(f"- {action[0]}")
            else:
                print(f"- {action}")
        print("- Open inventory")
        print("- Enter Q to quit")

        # Sets action variable to input
        action = input("What would you like to do? ").lower()

        # Pick up items
        if action == "pick up items":
            player.pick_up_item(room_list[current_room])

        # Open inventory
        elif action == "open inventory":
            player.open_inventory()

        # Check health
        elif action == "check health":
            player.check_health()

        # Move to another room
        elif action in ["go north", "go northeast", "go northwest", "go east",
                        "go south", "go southeast", "go southwest", "go west",
                        "go up", "go down"]:
            for a in actions:
                if isinstance(a, tuple) and action == a[0].lower():
                    next_room = a[1]
                    if next_room is not None and next_room < len(room_list):
                        current_room = next_room
                        break  # Exit the loop after finding the correct direction
            else:
                print("You cannot go that way.")

        # Use bandages
        elif action == "use bandages":
            player.use_bandages()

        # Solve riddle
        elif action == "solve riddle" and room_list[current_room].is_treasure_room:
            if room_list[current_room].riddle:
                answer = input("Enter the missing word from the riddle: ").lower()
                if answer == "understanding":
                    print("Congratulations! You have solved the riddle and unlocked the treasure!")
                    # Additional actions after solving the riddle, such as obtaining the treasure
                    print("You have beaten the game. Thanks for Playing!")
                    break
                else:
                    print("Incorrect answer. Keep trying or explore other rooms.")

        # Quit Option
        elif action == 'q':
            # Prints Quit Confirmation
            print("You decided to quit the game.")
            # Sets done to True and ends program.
            done = True

        # If input is not valid option
        else:
            print("Please enter a valid action.")
            # Continues Program
            continue


# Ends main function
main()
