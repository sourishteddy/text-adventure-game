# adventure.py

class Inventory:
    """Manages the player's inventory."""
    def __init__(self):
        self.items = []

    def add(self, item):
        print(f"You have received a [{item}].")
        self.items.append(item)

    def has(self, item):
        return item in self.items

class GameState:
    """Manages the state of the game, including location and inventory."""
    def __init__(self):
        self.inventory = Inventory()
        self.current_location = 'crossroads'
        self.game_is_over = False
        self.cellar_key_found = False

    def end_game(self, message):
        print(message)
        self.game_is_over = True

def get_player_choice(prompt="> "):
    """Gets and cleans player input, checking for a quit command."""
    choice = input(prompt).strip().lower()
    if choice in ['quit', 'exit']:
        return 'quit'
    return choice

def print_invalid_choice():
    """Prints a message for an invalid choice."""
    print("Invalid choice. Please try again.")

def handle_crossroads(state):
    """Handles logic for the crossroads location."""
    scene_description = (
        "You find yourself at a crossroads. A path leads to a dark cave to your left,\n"
        "and to your right, you see an enchanted forest. There is a strange marking on the ground."
    )
    print("\n" + scene_description)
    
    while True:
        print("\nWhat do you do?")
        print("1. Enter the dark cave.")
        print("2. Go into the enchanted forest.")
        print("3. Examine the marking.")
        print("Type 'look' to see the description again.")
        
        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "cave" in choice:
            state.current_location = 'dark_cave'
            return
        elif "2" in choice or "forest" in choice:
            state.current_location = 'enchanted_forest'
            return
        elif "3" in choice or "marking" in choice:
            state.current_location = 'hidden_cellar'
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def handle_dark_cave(state):
    """Handles logic for the dark cave."""
    scene_description = (
        "\nThe cave is dark and you hear the dripping of water.\n"
        "You can see a faint light deeper inside."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Go towards the light.")
        print("2. Go back to the crossroads.")
        print("Type 'look' to see the description again.")

        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "light" in choice:
            state.current_location = 'ancient_ruins'
            return
        elif "2" in choice or "back" in choice:
            print("\nYou decide the cave is too dangerous and return to the crossroads.")
            state.current_location = 'crossroads'
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def handle_enchanted_forest(state):
    """Handles logic for the enchanted forest."""
    scene_description = (
        "\nThe trees in the forest have glowing leaves, and the air hums with magic.\n"
        "You see a mischievous pixie watching you from a branch."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Try to talk to the pixie.")
        print("2. Ignore the pixie and walk deeper into the forest.")
        print("Type 'look' to see the description again.")

        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "talk" in choice:
            print("\nThe pixie giggles and offers you a glowing fruit. 'It might help in the dark,' it whispers.")
            state.inventory.add("Glowing Fruit")
            print("The pixie points you toward a murky swamp.")
            state.current_location = 'murky_swamp'
            return
        elif "2" in choice or "ignore" in choice:
            state.end_game("\nThe pixie gets angry at being ignored and casts a spell on you.\nYou are turned into a frog. GAME OVER. 🐸")
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def handle_ancient_ruins(state):
    """Handles logic for the ancient ruins."""
    scene_description = (
        "\nYou stumble upon the ruins of an ancient civilization.\n"
        "A large stone tablet with faint carvings stands in the center."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Read the tablet.")
        print("2. Search the surrounding area for treasure.")
        print("Type 'look' to see the description again.")
        
        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "read" in choice:
            print("\nThe tablet tells a story of a hidden artifact with immense power.")
            print("As you finish reading, a hidden compartment in the tablet slides open.")
            state.inventory.add("Lost Diadem of the Ancients")
            state.end_game("You've found the artifact! You WIN! 🎉")
            return
        elif "2" in choice or "search" in choice:
            state.end_game("\nYou search the ruins but find only rocks and dust.\nAs you dig, you trigger a hidden trap, and the ruins begin to collapse around you.\nYou don't make it out in time. GAME OVER. 💀")
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def handle_hidden_cellar(state):
    """Handles logic for the hidden cellar."""
    scene_description = (
        "\nYou push on the marking and a stone slab slides away, revealing a dark, dusty cellar.\n"
        "In the center of the room is a large, locked chest."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Try to open the chest.")
        print("2. Search the dusty corners of the cellar.")
        print("3. Leave the cellar.")
        print("Type 'look' to see the description again.")

        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "open" in choice:
            if state.inventory.has("Old Key"):
                print("\nYou use the [Old Key] you found. The lock clicks open!")
                state.inventory.add("Ancient Map")
                state.end_game("Inside, you find an ancient map to a forgotten kingdom! You WIN! 🗺️")
                return
            else:
                print("\nThe chest is locked tight. You need a key.")
        elif "2" in choice or "search" in choice:
            if not state.cellar_key_found:
                print("\nYou search through cobwebs and dust, and find an [Old Key] hidden under a loose floorboard!")
                state.inventory.add("Old Key")
                state.cellar_key_found = True
            else:
                print("\nYou've already searched the cellar and found the key.")
        elif "3" in choice or "leave" in choice:
            print("\nYou climb back out to the crossroads.")
            state.current_location = 'crossroads'
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def handle_murky_swamp(state):
    """Handles logic for the murky swamp."""
    scene_description = (
        "\nThe path leads you to a swamp shrouded in a thick, magical fog.\n"
        "You can't see more than a few feet ahead of you. It's too dangerous to walk blindly."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Try to walk through the fog.")
        print("2. Go back to the forest.")
        if state.inventory.has("Glowing Fruit"):
            print("3. Use the Glowing Fruit.")
        print("Type 'look' to see the description again.")

        choice = get_player_choice()

        if choice == 'quit':
            state.end_game("You leave the adventure behind.")
            return
        elif "1" in choice or "walk" in choice:
            state.end_game("\nYou try to navigate the fog but quickly get lost and sink into the mire. GAME OVER. 💀")
            return
        elif "2" in choice or "back" in choice:
            print("\nYou return to the enchanted forest.")
            state.current_location = 'enchanted_forest'
            return
        elif ("3" in choice or "fruit" in choice) and state.inventory.has("Glowing Fruit"):
            print("\nYou hold up the [Glowing Fruit]. Its gentle light cuts through the magical fog, revealing a safe stone path!")
            state.end_game("You safely cross the swamp. You WIN! ✨")
            return
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print_invalid_choice()

def play_adventure_game():
    """The main entry point and game loop for the adventure."""
    print("Welcome to the Enhanced Adventure Game!")
    
    state = GameState()
    
    # This is the main game loop. It runs as long as the game isn't over.
    while not state.game_is_over:
        if state.current_location == 'crossroads':
            handle_crossroads(state)
        elif state.current_location == 'dark_cave':
            handle_dark_cave(state)
        elif state.current_location == 'enchanted_forest':
            handle_enchanted_forest(state)
        elif state.current_location == 'ancient_ruins':
            handle_ancient_ruins(state)
        elif state.current_location == 'hidden_cellar':
            handle_hidden_cellar(state)
        elif state.current_location == 'murky_swamp':
            handle_murky_swamp(state)