'''
Module with main classes of the game.
'''
class Room:
    '''
    Class to create and initialize the room.
    >>> kitchen = Room('Kitchen')
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> print(kitchen)
    A dank and dirty room buzzing with flies.
    '''
    def __init__(self, name):
        '''
        Initializes the room.
        '''
        self.name = name
        self.description = None
        self.connections = {}
        self.characters = []
        self.items = []

    def set_description(self, description):
        '''
        Sets description to the roon.
        '''
        self.description = description

    def link_room(self, direction, room):
        '''
        Adds connection between two rooms.
        '''
        self.connections[direction] = room
    
    def set_character(self, ch):
        '''
        Adds character to the room.
        '''
        self.characters.append(ch)

    def remove_character(self, character):
        '''
        Removes character from the room.
        '''
        self.characters.remove(character)

    def set_item(self, item):
        '''
        Appends item to the room.
        '''
        self.items.append(item)

    def remove_item(self, item):
        '''
        Removes item from the room.
        '''
        self.items.remove(item)

    def get_details(self):
        '''
        Returns detailes about the current room.
        '''
        return f'{self.name} has ilems {self.items}, characters {self.characters} and\
 is connected to {self.connections}.'

    def get_character(self):
        '''
        Returns character that is in current room.
        '''
        if len(self.characters) != 0:
            return self.characters[0]
        return None
    
    def get_item(self):
        '''
        Returns item from the current room.
        '''
        if len(self.items) != 0:
            return self.items[0]
        return None
    
    def move(self, direction):
        '''
        Method to move from one room to another.
        '''
        if direction in self.connections:
            return self.connections[direction]

    def __str__(self):
        '''
        Returns the string representation of the room.
        '''
        return f'{self.description}'

class Character:
    '''
    Creates and initializes the character.
    >>> char = Character("Tabitha", "An enormous spider with countless eyes and furry legs.")
    >>> print(char)
    Tabitha
    '''
    def __init__(self, name, description):
        '''
        Initializes the data.
        '''
        self.name = name
        self.description = description
        self.talk_response = None

    def set_conversation(self, speech):
        '''
        Returns talk of the person.
        '''
        self.talk_response = speech
        return speech

    def describe(self):
        '''
        Returns the description of the character.
        '''
        return self.description
    
    def talk(self):
        '''
        Returns conversation of the character if it is not None.
        '''
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def __str__(self):
        '''
        Returns string with character name.
        '''
        return self.name

class Enemy(Character):
    '''
    Class to create and initialize the enemy.
    '''
    def __init__(self, name, description):
        '''
        Initializes the data.
        '''
        super().__init__(name, description)
        self.weakness = None

    def fight(self, combat_item):
        '''
        Method to fight with enemy.
        '''
        if combat_item == self.weakness:
            return True
        return False

    def set_weakness(self, item):
        '''
        Method to set the weakness (item) of the character. 
        '''
        self.weakness = item

    def get_weakness(self):
        '''
        Returns the weakness of the enemy.
        '''
        return self.weakness


class Friend(Character):
    '''
    Class to create and initialize a friend.
    '''
    def __init__(self, name, description, gift_item):
        '''
        Initialize the data.
        '''
        super().__init__(name, description)
        self.gift_item = gift_item

    def give_gift(self):
        '''
        Method to gift :)
        '''
        return self.gift_item

class Item:
    '''
    Class to create and initialize the item.
    '''
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def set_description(self, text):
        '''
        Adds description to the item.
        '''
        self.description = text

    def __str__(self):
        '''
        Returns the string with name of item.
        '''
        return self.name



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
