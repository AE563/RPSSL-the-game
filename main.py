from player_input import player_choice
from computer_options import computer_choice, computer_opponent
from determine_winner import who_won
from announce import announce_opponent, announce_winner


opponent = computer_opponent()

announce_opponent(opponent)

player_fighter = player_choice()

computer_fighter = computer_choice(opponent, player_fighter)

winner = who_won(player_fighter, computer_fighter)

announce_winner(opponent, player_fighter, computer_fighter, winner)
