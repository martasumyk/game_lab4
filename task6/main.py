import task6

univercity = task6.Location('UCU')
univercity.set_description('The best univercity of Ukraine :)')

centre = task6.Location('City centre')
centre.set_description('The main city centre.')

current_location = univercity
backpack = []

dead = False

while dead == False:

    print("\n")
    print(current_location)

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        print(inhabitant)

    item = current_location.get_item()
    if item is not None:
        print(item)

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_location = current_location.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_location.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_location.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
