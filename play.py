def play(player1_choice, player2_choice):

    winning_combinations = {"rock": "scissor", "paper": "rock", "scissor": "paper"}

    if winning_combinations[player1_choice] == player2_choice:
        print(f"{player1_choice} beats {player2_choice}")
        print("Player 1 won")
    elif player1_choice == player2_choice:
        print("It's a draw, try again!!")
    else:
        print(f"{player2_choice} beats {player1_choice}")
        print("Player 2 won")
