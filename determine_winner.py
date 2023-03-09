import main
print(main.player_fighter)
print(computer_fighter)



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


def who_won():
    if player_fighter == computer_fighter:
        return 'Dead heat'

    elif computer_fighter in winner_loser_hashmap.get(player_fighter):
        return 'Player WON!'

    return 'Computer WON!'
