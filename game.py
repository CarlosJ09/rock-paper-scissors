class Game:
    def __init__(self):
        self.winning_combinations = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper",
        }

    def play(self, player1, player2):
        player1_choice = player1.make_choice()
        player2_choice = player2.make_choice()

        print(f"\n{player1.name} chose {player1_choice}")
        print(f"{player2.name} chose {player2_choice}")

        if self.winning_combinations[player1_choice] == player2_choice:
            print(f"{player1_choice} beats {player2_choice}. {player1.name} won!\n")
        elif player1_choice == player2_choice:
            print("It's a draw, try again!\n")
        else:
            print(f"{player2_choice} beats {player1_choice}. {player2.name} won!\n")
