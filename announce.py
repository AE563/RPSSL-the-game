from time import sleep


def announce_opponent(opponent):
    print(f"Your opponent is: {opponent}")
    sleep(0.6)
    print(f'{opponent} made a choice...\n')
    print('________________________________')
    sleep(1.2)


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
