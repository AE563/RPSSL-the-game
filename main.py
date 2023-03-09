import player_input
import computer_options
import determine_winner
import announce

player_fighter = player_input.player_choice()

computer_fighter = computer_options.computer_choice()

winner = determine_winner.who_won(player_fighter, computer_fighter)

announce.announce_winner(player_fighter, computer_fighter, winner)
