from time import sleep


def announce_winner(player_fighter, computer_fighter, winner):
    countdown = 3
    delay = 0.5

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay)
        countdown -= 1

    print(f'The player chose: {player_fighter} \nComputer chose:   {computer_fighter}\n\n>>>{winner}<<<')
