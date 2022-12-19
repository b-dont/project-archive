import random
from sys import exit

need_roll = True

while need_roll:

    roll = input("> ")
    part = roll.split('+')
    num_dice, num_sides = part[0].split('d')
    bonus = part[1]
    
    num_dice = int(num_dice)
    bonus = int(bonus)
    result = 0
    
    if roll == "q":
        exit()

    while num_dice >= 1:
        result += random.randint(1, int(num_sides))
        num_dice -= 1
    print(result + bonus)
