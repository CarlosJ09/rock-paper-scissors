import random
from play import play


def main():
    hello_message = "Select an option: \n\n1. Play vs CPU\n2. Multiplayer \n3. Quit"
    player1_choice = ""
    player2_choice = ""
    option = "0"

    while True:
        print(hello_message)
        option = input()

        if option == "1":
            print("type rock, scissor or paper")
            player1_choice = input()
            player2_choice = random.choice(["rock", "paper", "scissor"])

            print(f"The CPU choose {player2_choice}")

            play(player1_choice, player2_choice)

            option = "0"

        elif option == "2":
            print("Player 1, type rock, scissor or paper")
            player1_choice = input()
            print("Player 2, type rock, scissor or paper")
            player2_choice = input()

            play(player1_choice, player2_choice)

            option = "0"
        else:
            exit()


main()
