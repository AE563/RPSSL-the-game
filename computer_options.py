import random

# Chances are written as int(0-100)
# Calculated as percentages 5 -> 5%.
# They summ must by == 100%.
drop_chance_hashmap = {
    'Norman Reedus': {
        'Rock': 20,
        'Paper': 20,
        'Scissors': 20,
        'Spock': 20,
        'Lizard': 20
    },
    'Chris Rock': {
        'Rock': 60,
        'Paper': 10,
        'Scissors': 10,
        'Spock': 10,
        'Lizard': 10
    },
    'Leonard Nimoy': {
        'Rock': 10,
        'Paper': 25,
        'Scissors': 10,
        'Spock': 30,
        'Lizard': 25
    },
    # 'Loki Odinson': {
    #     'Rock': 0,
    #     'Paper': 0,
    #     'Scissors': 0,
    #     'Spock': 0,
    #     'Lizard': 0
    #     }
}

chance_pick_opponent_hashmap = {
    'Norman Reedus': 40,
    'Chris Rock': 30,
    'Leonard Nimoy': 30,
    # 'Loki Odinson': 10
    # 'Sonny' : 20
}


def computer_opponent():
    # Get the chances of the appearance of opponents
    chance_pick_norman = 100 - chance_pick_opponent_hashmap.get('Norman Reedus')
    chance_pick_chris = chance_pick_norman - chance_pick_opponent_hashmap.get('Chris Rock')
    chance_pick_leonard = chance_pick_chris - chance_pick_opponent_hashmap.get('Leonard Nimoy')
    # chance_pick_loki = chance_pick_leonard - chance_pick_opponent_hashmap.get('Loki Odinson')

    y = random.randint(1, 100)
    if y > chance_pick_norman:
        return 'Norman Reedus'
    elif y > chance_pick_chris:
        return 'Chris Rock'
    elif y > chance_pick_leonard:
        return 'Leonard Nimoy'
    else:
        return 'Loki Odinson'


def computer_choice(opponent):
    # Get the chances of the dropped opponent
    drop_chance_opponent = drop_chance_hashmap.get(opponent)
    drop_chance_rock = 100 - drop_chance_opponent.get('Rock')
    drop_chance_paper = drop_chance_rock - drop_chance_opponent.get('Paper')
    drop_chance_scissors = drop_chance_paper - drop_chance_opponent.get('Scissors')
    drop_chance_spock = drop_chance_scissors - drop_chance_opponent.get('Spock')

    y = random.randint(1, 100)
    if y > drop_chance_rock:
        return 'Rock'
    elif y > drop_chance_paper:
        return 'Paper'
    elif y > drop_chance_scissors:
        return 'Scissors'
    elif y > drop_chance_spock:
        return 'Spock'
    else:
        return 'Lizard'
