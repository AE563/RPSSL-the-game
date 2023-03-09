from time import sleep

import player_input
import computer_options
import determine_winner
player_fighter = player_input.player_choice()

computer_fighter = computer_options.computer_choice()

# winner_loser_hashmap = {
#     'Rock': [
#         'Scissors',
#         'Lizard'
#     ],
#     'Paper': [
#         'Rock',
#         'Spock'
#     ],
#     'Scissors': [
#         'Paper',
#         'Lizard'
#     ],
#     'Spock': [
#         'Paper',
#         'Rock'
#     ],
#     'Lizard': [
#         'Paper',
#         'Spock'
#     ]
# }
#
#
# def who_won():
#     if player_fighter == computer_fighter:
#         return 'Dead heat'
#
#     elif computer_fighter in winner_loser_hashmap.get(player_fighter):
#         return 'Player WON!'
#
#     return 'Computer WON!'


winner = determine_winner.who_won()


def announce_winner():
    countdown = 3
    delay = 0.5

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'The player chose: {player_fighter} \nComputer chose:   {computer_fighter}\n\n>>>{winner}<<<')


announce_winner()
