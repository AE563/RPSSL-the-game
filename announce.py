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


def announce_winner(opponent, player_fighter, computer_fighter, winner):
    countdown = 3
    delay = 0.5
    print()

    if winner == 'draw':
        announce = 'Draw'

    elif winner == 'player_win':
        announce = 'Player WON!'

    else:
        announce = f'{opponent} WON!'

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'{opponent} chose:   {computer_fighter}\nThe player chose: {player_fighter} ')
    sleep(delay)
    print(f'\n>>> {announce} <<<')
