"""Game"""

win_rate = 0

class Room:
    """Class Room"""
    def __init__(self, name):
        """init"""
        self.name = name
        self.room_description = ""
        self.item = None
        self.character = None
        self.linked_rooms = []
        self.current_room = None

    def set_description(self, room_description):
        """Function set description"""
        self.room_description = room_description

    def link_room(self, name_room, direction):
        """Funktion link rooms"""
        self.linked_rooms.append((name_room, direction))

    def set_item(self, item):
        """Function set item"""
        self.item = item

    def set_character(self, character):
        """Function set character"""
        self.character = character

    def get_details(self):
        """Fuction to get details of the room"""
        print(self.name)
        print("--------------------")
        print(self.room_description)
        for room in self.linked_rooms:
            print(f"The {room[0].name} is {room[1]}")

    def get_character(self):
        """Function to find out what the character"""
        return self.character

    def get_item(self):
        """Function to find out what the item"""
        return self.item

    def move(self, direct_to_go):
        """Function to move among rooms"""
        for room in self.linked_rooms:
            if room[1] == direct_to_go:
                return room[0]

class Stryi(Room):
    """class Stryi"""
    def get_info(self):
        """get info"""
        print("Welcome to my game!")
        print("You have a few locations, where there are weapons and enemies.")
        print("Your main goal to kill putin.")
        print("To win the game you should defeat all the enemies.")
        print("Good luck!")
        print()

class Character:
    """Class Character"""
    def __init__(self, name, description):
        """init"""
        self.name = name
        self.description = description
        self.phrase_conversation = ""

    def set_conversation(self, phrase_conversation):
        """Function to set conversation"""
        self.phrase_conversation = phrase_conversation

    def describe(self):
        """Function that describes character"""
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """Function to talk"""
        print(f"[{self.name} says]: {self.phrase_conversation}")


class Enemy(Character):
    """Class Enemy"""
    def __init__(self, enemy_name, enemy_description):
        """init"""
        super().__init__(enemy_name, enemy_description)
        self.weakness = []

    def set_weakness(self, weakness):
        """Function to set weakness"""
        self.weakness.append(weakness)

    def fight(self, item):
        """Function that check the weakness and if
        win add the point to win rate"""
        global win_rate
        if item in self.weakness:
            win_rate += 1
            return True
        return False

    @classmethod
    def get_defeated(cls):
        """Function returns win rate"""
        global win_rate
        return win_rate

class Friend(Character):
    """Class Friend """
    def __init__(self, friend_name, friend_description):
        """init"""
        super().__init__(friend_name, friend_description)

    @classmethod
    def give_you_weapon(cls):
        """friend give you weapon"""
        print("[Lera]: Hello, don't be afraid, I'm your friend!")
        print("My gift is in your backpack.")

class Item:
    """Class Item"""
    def __init__(self, item_name):
        """init"""
        self.item_name = item_name
        self.item_description = ""

    def set_description(self, item_description):
        """set description"""
        self.item_description = item_description

    def get_name(self):
        """get name"""
        return self.item_name

    def describe(self):
        """describes"""
        print(f"The [{self.item_name}] is here - {self.item_description}")

class Super_Weapon(Item):
    """Class Super Weapon"""
    def __init__(self, weapon_name):
        """init"""
        super().__init__(weapon_name)
