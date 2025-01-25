import random

winning_combinations = {"rock": "scissor", "paper": "rock", "scissor": "paper"}


class Choice:
    def __init__(self, choice: str, attempt: int):
        self.choice = choice
        self.attempt = attempt


class Paper(Choice):
    def __init__(self):
        self.choice = "paper"
        pass


class Rock(Choice):
    def __init__(self):
        self.choice = "rock"
        pass


class Scissors(Choice):
    def __init__(self):
        self.choice = "scissor"
        pass


def main():
    option = "0"
    hello_message = "Select an option: \n\n1. Play vs CPU\n2. Multiplayer \n3. Quit"
    player1_choice = ""
    player2_choice = ""
    bot_choice = ""

    while True:
        print(hello_message)
        option = input()

        if option == "1":
            print("type rock, scissor or paper")
            player1_choice = input()
            bot_choice = random.choice(["rock", "paper", "scissor"])

            print(f"The CPU choose {bot_choice}")

            if(winning_combinations[player1_choice] == bot_choice):
                print(f"{player1_choice} beats {bot_choice}")
                print("Player1 won")
            elif(player1_choice == bot_choice):
                print("It's a draw, try again!!")
            else:
                print(f"{bot_choice} beats {player1_choice}")
                print("CPU won")
                option = "0"


        elif option == "2":
            print("hello")
            option = "0"
        else:
            exit()


main()
