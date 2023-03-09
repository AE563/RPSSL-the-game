from player_input import player_choice
from computer_options import computer_choice
from determine_winner import who_won
from announce import announce_winner


player_fighter = player_choice()

computer_fighter = computer_choice()

winner = who_won(player_fighter, computer_fighter)

announce_winner(player_fighter, computer_fighter, winner)
