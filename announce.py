from time import sleep

dictionary_fighter = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Spock',
    5: 'Lizard'
}


def announce_opponent(opponent):
    print(f"Your opponent is: {opponent}")
    sleep(0.6)
    print(f'{opponent} made a choice...\n')
    print('________________________________')
    sleep(1)


def announce_player_input():
    print('Choose your fighter (ง •̀_•́)ง')
    for k, v in dictionary_fighter.items():
        print(k, ':', v)


def announce_round_winner(opponent, player_fighter, computer_fighter, winner):
    countdown = 3
    delay = 0.5
    print()

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    if winner == 'draw':
        announce = 'Draw'

    elif winner == 'player_win':
        announce = 'Player WON!'

    else:
        announce = f'{opponent} WON!'

    print(f'{opponent} chose:   {computer_fighter}\nThe player chose: {player_fighter} ')
    sleep(delay)
    print(f'\n>>> {announce} <<<')
    print('________________________________')


# def announce_game_winner(player_score, computer_score):
#     if player_score == 3:
#         return print(f'The player won this game with a score:{player_score}:{computer_score}')
#     if computer_score == 3:
#         return print(f'The computer won this game with a score:{computer_score}:{player_score}')
