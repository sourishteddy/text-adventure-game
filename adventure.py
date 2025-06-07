inventory = []


def start_game():
    global inventory
    inventory = []

    scene_description = (
        "Welcome to the Enhanced Adventure Game! \n"
        "You find yourself at a crossroads. A path leads to a dark cave to your left,\n"
        "and to your right, you see an enchanted forest. There is a strange marking on the ground."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Enter the dark cave.")
        print("2. Go into the enchanted forest.")
        print("3. Examine the marking.")
        print("Type 'look' to see the description again.")

        choice = input("> ").lower()

        if "1" in choice or "cave" in choice:
            dark_cave()
            break
        elif "2" in choice or "forest" in choice:
            enchanted_forest()
            break
        elif "3" in choice or "marking" in choice:
            hidden_cellar()
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


def dark_cave():
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

        choice = input("> ").lower()

        if "1" in choice or "light" in choice:
            ancient_ruins()
            break
        elif "2" in choice or "back" in choice:
            print("\nYou decide the cave is too dangerous and return to the crossroads.")
            start_game()
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


def enchanted_forest():
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

        choice = input("> ").lower()

        if "1" in choice or "talk" in choice:
            print("\nThe pixie giggles and offers you a glowing fruit. 'It might help in the dark,' it whispers.")
            print("You have received a [Glowing Fruit].")
            inventory.append("Glowing Fruit")
            print("The pixie points you toward a murky swamp.")
            murky_swamp()
            break
        elif "2" in choice or "ignore" in choice:
            print("\nThe pixie gets angry at being ignored and casts a spell on you.")
            print("You are turned into a frog. GAME OVER. 🐸")
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


def ancient_ruins():
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

        choice = input("> ").lower()

        if "1" in choice or "read" in choice:
            print("\nThe tablet tells a story of a hidden artifact with immense power.")
            print("As you finish reading, a hidden compartment in the tablet slides open.")
            print("You've found the [Lost Diadem of the Ancients]! You WIN! 🎉")
            inventory.append("Lost Diadem")
            break
        elif "2" in choice or "search" in choice:
            print("\nYou search the ruins but find only rocks and dust.")
            print("As you dig, you trigger a hidden trap, and the ruins begin to collapse around you.")
            print("You don't make it out in time. GAME OVER. 💀")
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


def hidden_cellar():
    scene_description = (
        "\nYou push on the marking and a stone slab slides away, revealing a dark, dusty cellar.\n"
        "In the center of the room is a large, locked chest."
    )
    print(scene_description)

    has_found_key = False

    while True:
        print("\nWhat do you do?")
        print("1. Try to open the chest.")
        print("2. Search the dusty corners of the cellar.")
        print("3. Leave the cellar.")
        print("Type 'look' to see the description again.")

        choice = input("> ").lower()

        if "1" in choice or "open" in choice:
            if "Old Key" in inventory:
                print("\nYou use the [Old Key] you found. The lock clicks open!")
                print("Inside, you find an ancient map to a forgotten kingdom! You WIN! 🗺️")
                inventory.append("Ancient Map")
                break
            else:
                print("\nThe chest is locked tight. You need a key.")
        elif "2" in choice or "search" in choice:
            if not has_found_key:
                print("\nYou search through cobwebs and dust, and find an [Old Key] hidden under a loose floorboard!")
                inventory.append("Old Key")
                has_found_key = True
            else:
                print("\nYou've already searched the cellar and found the key.")
        elif "3" in choice or "leave" in choice:
            print("\nYou climb back out to the crossroads.")
            start_game()
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


def murky_swamp():
    scene_description = (
        "\nThe path leads you to a swamp shrouded in a thick, magical fog.\n"
        "You can't see more than a few feet ahead of you. It's too dangerous to walk blindly."
    )
    print(scene_description)

    while True:
        print("\nWhat do you do?")
        print("1. Try to walk through the fog.")
        print("2. Go back to the forest.")
        if "Glowing Fruit" in inventory:
            print("3. Use the Glowing Fruit.")
        print("Type 'look' to see the description again.")

        choice = input("> ").lower()

        if "1" in choice or "walk" in choice:
            print("\nYou try to navigate the fog but quickly get lost and sink into the mire. GAME OVER. 💀")
            break
        elif "2" in choice or "back" in choice:
            print("\nYou return to the enchanted forest.")
            enchanted_forest()
            break
        elif ("3" in choice or "fruit" in choice) and "Glowing Fruit" in inventory:
            print("\nYou hold up the [Glowing Fruit]. Its gentle light cuts through the magical fog, revealing a safe stone path!")
            print("You safely cross the swamp. You WIN! ✨")
            break
        elif "look" in choice:
            print("\n" + scene_description)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start_game()