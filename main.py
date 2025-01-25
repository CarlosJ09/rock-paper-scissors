from player import Player
from game import Game

def main():
    print("Welcome to Rock-Paper-Scissors!")
    game = Game()

    while True:
        print("\nSelect an option:\n1. Play vs CPU\n2. Multiplayer\n3. Quit\n")
        option = input()

        if option == "1":
            player1 = Player(name="Player 1")
            player2 = Player(name="CPU", is_cpu=True)
            game.play(player1, player2)
        elif option == "2":
            player1 = Player(name="Player 1")
            player2 = Player(name="Player 2")
            game.play(player1, player2)
        elif option == "3":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()

