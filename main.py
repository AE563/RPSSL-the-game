import random
from time import sleep

dictionary_fighter = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Spock',
    5: 'Lizard'
}


def player_choice():
    print('(ง •̀_•́)ง')
    for k, v in dictionary_fighter.items():
        print(k, ':', v)
    return int(input('Choose your fighter, enter the number:'))


player_fighter = dictionary_fighter[player_choice()]


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


computer_fighter = computer_choice()

winner_loser_hashmap = {
    'Rock': [
        'Scissors',
        'Lizard'
    ],
    'Paper': [
        'Rock',
        'Spock'
    ],
    'Scissors': [
        'Paper',
        'Lizard'
    ],
    'Spock': [
        'Paper',
        'Rock'
    ],
    'Lizard': [
        'Paper',
        'Spock'
    ]
}


def determine_winner():
    if player_fighter == computer_fighter:
        return 'Dead heat'

    elif computer_fighter in winner_loser_hashmap.get(player_fighter):
        return 'Player WON!'

    return 'Computer WON!'


winner = determine_winner()


def announce_winner():
    countdown = 3
    delay = 0.5

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'The player chose: {player_fighter} \nComputer chose:   {computer_fighter}\n\n>>>{winner}<<<')


announce_winner()
