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


def who_won(player_fighter, computer_fighter):
    if player_fighter == computer_fighter:
        return 'draw'

    elif computer_fighter in winner_loser_hashmap.get(player_fighter):
        return 'player_win'

    return 'computer_win'
