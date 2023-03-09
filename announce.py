from time import sleep


def announce_winner(player_fighter, computer_fighter, winner):
    countdown = 3
    delay = 0.5
    print()

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'Computer chose:   {computer_fighter}\nThe player chose: {player_fighter} ')
    sleep(1.2)
    print(f'\n>>> {winner} <<<')
