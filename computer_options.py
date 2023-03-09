import random


def computer_opponent():
    y = random.randint(1, 100)
    if y > 60:
        return 'Norman Reedus'
    elif y > 30:
        return 'Chris Rock'
    elif y > 10:
        return 'Leonard Nimoy'
    else:
        return 'Loki Odinson'


def computer_choice():
    y = random.randint(1, 100)
    if y > 80:
        return 'Rock'
    elif y > 60:
        return 'Paper'
    elif y > 40:
        return 'Scissors'
    elif y > 20:
        return 'Spock'
    else:
        return 'Lizard'
