"""game"""
import game6

# locations
stryi = game6.Stryi("Stryi")
stryi.set_description("A beautiful town that has its long history.")
stryi.get_info()

kyiv = game6.Room("Kyiv")
kyiv.set_description("The capital of Ukraine, the most important place.")

odesa = game6.Room("Odessa")
odesa.set_description("The beautiful city near the sea.")

chorobaivka = game6.Room("Chorobaivka")
chorobaivka.set_description("The town which has more parts that any movie series.")

lviv = game6.Room("Lviv")
lviv.set_description("The city, where the rain is a routine, second London.")

moskwa = game6.Room("moskva")
moskwa.set_description("The city where you can see a dead body in the square")

stryi.link_room(lviv, "north")
lviv.link_room(chorobaivka, "south")
chorobaivka.link_room(lviv, "north")
chorobaivka.link_room(odesa, "south")
odesa.link_room(chorobaivka, "east")
odesa.link_room(lviv, "north-west")
odesa.link_room(kyiv, "north")
kyiv.link_room(moskwa, "east")
kyiv.link_room(odesa, "south")

# items
kalash = game6.Item("Kalash")
kalash.set_description("Very good weapon for russian soldier.")

javelin = game6.Item("Javelin")
javelin.set_description("The weapon with what you can kill another soldier.")
lviv.set_item(javelin)

neptun = game6.Item("Neptun")
neptun.set_description("The rocket which is good at sink the ship.")
chorobaivka.set_item(neptun)

bayraktar = game6.Item("Bayraktar")
bayraktar.set_description("The weapon with what you can destroy army in Kyiv.")
odesa.set_item(bayraktar)

nuke = game6.Super_Weapon("Nuke")
nuke.set_description("The weapon with what you can kill the boss and his country.")
kyiv.set_item(nuke)

# enemies
russian_soldier = game6.Enemy("Tolya", "A smelly russian.")
russian_soldier.set_conversation("Hello, I'm stupid russian soldier.")
russian_soldier.set_weakness("Kalash")
russian_soldier.set_weakness("Nuke")
lviv.set_character(russian_soldier)

russian_soldiers = game6.Enemy("Convoy", "A smelly russians in car.")
russian_soldiers.set_conversation("Brbrbrbrbrbrbrbrbrbrb...")
russian_soldiers.set_weakness("Javelin")
russian_soldiers.set_weakness("Nuke")
chorobaivka.set_character(russian_soldiers)

korabel_moskwa = game6.Enemy("Moskwa-ship", "A smelly russian flagship.")
korabel_moskwa.set_conversation("We russian ship advice you to surender.")
korabel_moskwa.set_weakness("Neptun")
korabel_moskwa.set_weakness("Nuke")
odesa.set_character(korabel_moskwa)

russian_army = game6.Enemy("Army", "A smelly russian army.")
russian_army.set_conversation("We will take Kyiv in 3 days!")
russian_army.set_weakness("Bayraktar")
russian_army.set_weakness("Nuke")
kyiv.set_character(russian_army)

putin = game6.Enemy("Putin-Khuilo", "Russian fascist.")
putin.set_conversation("Nravitsa ne nravitsa terpi moja krasavica.")
putin.set_weakness("Nuke")
moskwa.set_character(putin)

# friend
friend = game6.Friend("Lera", "A girl with help")
friend.set_conversation("To win your enemies you need the weapon.\n"
                        "So I give it to you.")
stryi.set_character(friend)
friend.give_you_weapon()


current_room = stryi
backpack = []
backpack.append(kalash.item_name)

dead = False

while dead == False:

    print("\n")
    current_room.get_details()
    print()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    print("-----------")
    print("Choose the command:")
    print("- [north, south, east, west]: to move in chosen direction\n"
          "- talk: to talk with the character\n"
          "- fight: to fight with the enemy\n"
          "- take: to take the item\n"
          "- show: to show the items in backpack")
    print("-----------")

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            if current_room.get_character().name != "Lera":
                print("What will you fight with?")

                print("Items: " + ', '.join(map(str, backpack)))

                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 5:
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
                print("You cannot fight with friend.")
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "show":
        if len(backpack) == 0:
            print("There is no items in backpack")
        else:
            print(*backpack, sep = ", ")
    else:
        print("I don't know how to " + command)
