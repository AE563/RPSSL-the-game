from time import sleep


def announce_winner(opponent, player_fighter, computer_fighter, winner):
    countdown = 3
    delay = 0.5
    print()

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'{opponent} chose:   {computer_fighter}\nThe player chose: {player_fighter} ')
    sleep(delay)
    print(f'\n>>> {winner} <<<')
