'''
Module with main classes for the game.
'''
class Character:
    '''
    Class to create and initialize different characters.
    >>> person = Character('Ann')
    >>> person.set_description('A nice girl :)')
    >>> print(person.get_description())
    A nice girl :)
    '''
    def __init__(self, name, description=None, conversation=None):
        '''
        Initializes the data.
        '''
        self.name = name
        self.description = description
        self.conversation = conversation


    def set_description(self, description):
        '''
        Adds descriprion of the character.
        '''
        self.description = description

    def get_description(self):
        '''
        Returns description of the character.
        '''
        return self.description
    
    def set_conversation(self, speech):
        '''
        Add speech to the person.
        '''
        self.conversation = speech
    
    def get_conversation(self):
        '''
        Returns the speech of current person.
        '''
        return self.conversation
    
    def __str__(self):
        '''
        Returns the name of the character.
        '''
        return f'Name - {self.name}'


class Enemy(Character):
    '''
    Class to create and initialize enemy - the character that can attack you.
    >>> devil = Enemy('Jack', 'May attack you at night', 'Brrr', 'bows and arrows',\
 'rationalization')
    >>> print(devil)
    Enemy name - Jack, his defence - rationalization, his weapon - bows and arrows.
    '''
    def __init__(self, name, description, conversation, weapon=None, defence=None, health=3):
        '''
        Initializes the data.
        >>> devil = Enemy
        '''
        super().__init__(name, description, conversation)
        self.weapon = weapon
        self.defence = defence
        self.health = health
    
    def set_weapon(self, item):
        '''
        Method to set the weakness (item) of the character. 
        '''
        self.weapon = item

    def get_weapon(self):
        '''
        Returns the weakness of the enemy.
        '''
        return self.weapon
    
    def set_defence(self, item):
        '''
        Method to set the weakness (item) of the character. 
        '''
        self.defence = item

    def get_defence(self):
        '''
        Returns the weakness of the enemy.
        '''
        return self.defence
    
    def fight_with(self, item_weapon, item_defence):
        '''
        Method to fight with enemy.
        If his weapon is your defence and your weapon is not his defence, you win.
        '''
        if self.weapon == item_defence and item_weapon != self.defence:
            self.health -= 1
            return 'You win the enemy!'
        return 'You lost the enemy!'
    
    def __str__(self):
        '''
        Returns the string with info about the enemy.
        '''
        return f'Enemy name - {self.name}, his defence - {self.defence},\
 his weapon - {self.weapon}.'


class Friend(Character):
    '''
    Class to create and initialise friend - the character that may help you.
    >>> bro = Friend('Jude', 'Nice guy')
    >>> print(bro)
    Friend`s name - Jude and he/she can help you 3 times.
    '''
    def __init__(self, name, description=None, conversation=None, kindness=3):
        '''
        Initializes the data.
        '''
        super().__init__(name, description, conversation)
        self.kindness = kindness

    def hug(self):
        '''
        Increases your friend`s kindness.
        '''
        self.kindness += 1

    def help(self, enemy):
        '''
        Your friend may help you if you`re in good relations.
        '''
        enemy.health -= 1
        self.kindness -= 1
    
    def __str__(self):
        '''
        Returns the string representation of your friend.
        '''
        return f'Friend`s name - {self.name} and he/she can help you {self.kindness} times.'
    




class Location:
    '''
    Main class that creates and initializes locations of the game.
    >>> location = Location('UCU')
    >>> print(location)
    Name - UCU, characters - [], items - [].
    '''
    def __init__(self, location_name, description=None, connected_locations = {},\
                  characters = [], items = [], danger=0):
        '''
        Initializes the data.
        '''
        self.location_name = location_name
        self.description = description
        self.connected_locations = connected_locations
        self.characters = characters
        self.items = items
        self.danger = danger

    def set_description(self, description):
        '''
        Adds description to the location.
        '''
        self.description = description
    
    def get_description(self):
        '''
        Returns description of the location.
        '''
        return self.description
    
    def connect_locations(self, location_to_connect, direction):
        '''
        Connects two locations by the side.
        '''
        self.connect_locations[direction] = location_to_connect

    def set_character(self, character):
        '''
        Adds character to the location.
        '''
        self.characters.append(character)

    def remove_character(self, character):
        '''
        Removes character from the room.
        '''
        self.characters.remove(character)
    
    def get_charater(self):
        '''
        Returns the list of the characters on the location.
        '''
        if len(self.characters) != 0:
            return self.characters
        return f'Oopps, there aren`t anybode here!'
    
    def set_item(self, item):
        '''
        Adds item to the location.
        '''
        self.items.append(item)

    def remove_item(self, item):
        '''
        Removes item from the room.
        '''
        self.items.remove(item)
    
    def get_items(self):
        '''
        Shows all the items of a current location.
        '''
        return self.items

    def __str__(self):
        '''
        Returns the info about current location.
        '''
        return f'Name - {self.location_name}, characters - {self.characters},\
 items - {self.items}.'
    
