from player_input import player_choice
from computer_options import computer_choice, computer_opponent
from determine_winner import who_won
from announce import announce_winner

opponent = computer_opponent()
print(f"Your opponent is: {opponent}")
print(f'{opponent} made a choice...\n')

player_fighter = player_choice()

computer_fighter = computer_choice(opponent)

winner = who_won(opponent, player_fighter, computer_fighter)

announce_winner(opponent, player_fighter, computer_fighter, winner)
