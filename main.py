from player_input import player_choice
from computer_options import computer_choice, computer_opponent
from determine_winner import who_won
from announce import announce_opponent, announce_player_input, announce_round_winner


def round_play():
    player_score = 0
    computer_score = 0
    round_counter = 1

    opponent = computer_opponent()
    announce_opponent(opponent)

    while True:
        if player_score == 3:
            print(f'\nPlayer won this game with a score: {player_score}|{computer_score}')
            break
        if computer_score == 3:
            print(f'\n{opponent} won this game with a score: {computer_score}|{player_score}')
            break

        if round_counter >= 2:
            print(f'~ ROUND {round_counter} ~\n Player score: {player_score}\n {opponent} score: {computer_score}')

        announce_player_input()
        player_fighter = player_choice()
        computer_fighter = computer_choice(opponent, player_fighter)
        winner = who_won(player_fighter, computer_fighter)
        announce_round_winner(opponent, player_fighter, computer_fighter, winner)

        if winner == 'player_win':
            player_score += 1
        elif winner == 'computer_win':
            computer_score += 1
        round_counter += 1
    print('Thanks for the game! Submit your comments =^_ ^=')


round_play()
