from pprint import pprint
from sys import argv

class Character:
    def __init__(self, name: str, health: int, initiative: int):
        self.name = name
        self.health = health
        self.initiative = initiative
    
    def __lt__(self, other):
        return self.initiative < other.initiative
    
    def __eq__(self, other):
        return (self.initiative, self.name, self.health) == (other.initiative, other.name, other.health)

    def __str__(self):
        '''Converts to a string just as an integer'''
        return f'{self.name} - HP: {self.health} Initiative: {self.initiative}'

    def __repr__(self):
        return f'{self}'

def get_initiative(character):
    '''Get the initiative attribute of the Character classes'''
    return character.initiative

args = argv[1:]

characters = []

# if exicuted with command-line arguments
if args:
    for arg in args:
        name, health, initiative = arg.split(',')
        characters.append(Character(name=name, health=int(health), initiative=int(initiative)))
    characters = sorted(characters, key=get_initiative, reverse=True)
# if there are no command-line arguments
else:
    while True:

        # user inputs players and NPCs
        name = input("\nEnter name: ")
        health = int(input("Enter health: "))
        initiative = int(input("Enter initiative: "))

        # add characters to the characters list
        characters.append(Character(name=name, health=health, initiative=initiative))
        
        # sort the characters list from highest initiative to lowest
        characters = sorted(characters, key=get_initiative, reverse=True)

        # repeat input until user enters 'q' to start the 'turns' loop
        enter_character = input('''\n'Enter' key to add more Characters 'q' to finish: ''')
        if enter_character == 'q':
            break

        print('\nCharacters: \n', end='')
        pprint(characters)

first_character = characters[0]
round = 0

while True:
    # keep track of number of rounds
    if characters[0] is first_character:
        round += 1
        print(f'round {round}')
    print('\nCharacters: \n', end='')
    pprint(characters)

    # user input cycles through turns in initiative order, or adjusts character health values
    user_input = input('''
    Press 'Enter' to end the turn.
    To adjust health, type a character's name and '- damage value' or '+ healing value'.
    Example: 'Frodo + 10' or 'Frodo - 10'.
    ''')

    if user_input == '': # if user input empty, take the first item on the characters list and place it at the end
        characters.append(characters.pop(0))
    elif user_input == 'q': # quit with 'q' input
        break
    else: # adjust character health with user input

        # parse the user's input 
        character_name, dmg_or_heal, health_adjust = user_input.split()
        health_adjust = int(health_adjust)

        for character in characters:
            if character.name == character_name:
                if dmg_or_heal == '+':
                    character.health += health_adjust
                elif dmg_or_heal == '-':
                    character.health -= health_adjust

        print('\nCharacters: \n', end='')
        pprint(characters)
fatal: not a git repository (or any of the parent directories): .git
