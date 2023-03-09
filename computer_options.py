import random


def computer_choice():
    y = random.randint(1, 5)
    if y == 5:
        return 'Rock'
    elif y == 4:
        return 'Paper'
    elif y == 3:
        return 'Scissors'
    elif y == 2:
        return 'Spock'
    else:
        return 'Lizard'
