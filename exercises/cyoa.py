"""EX06 - Choose your own adventure."""

__author__: str = "730320104"

from random import randint

secret: int = randint(1, 100)

player: str = input("Hi, and welcome to NUMBER GOLF, the game show where you guess a randomly generated integer between 1 and 100 in the least amount of attempts. The goal of the game is to correctly guess the number and have the least amount of strokes. What is your name, contestant? ") 

x: int = 0

def greet(player: str) -> None:
    """Defined a function that greets a player when joining the game and helps them understand their first decision."""
    points: int = 0
    print(f"Ok {player}, let's begin the game! You have 3 options for your first 'shot': a) guess a random integer (+1 stroke), b) ask for a hint (+2 strokes), or c) give up (+1000 strokes). Please type your selection now: (a/b/c) ")
    y: str = input()
    if y == "a":
        points = points + 1
        f = int(input(f"What is your integer guess? "))
        if f < secret:
            print("Not quite. Guess a higher number.")
        if f > secret:
            print("Not quite. Guess a lower number.")
        if f == secret:
            print(f"You got it! Congratulations! Your total strokes was {points}.")
            quit()
    if y == "b":
        points = points + 2
        if secret <= 50:
            print("The secret number is less than or equal to 50.")
        else:
            print("The secret number is greater than 50.")
    if y == "c":
        points = points + 1000
        print(f"Thank you for playing. Your total strokes was {points}.")
        quit()


def main() -> None:
    """Defined the 'main' function of our game that runs and lets the player try to pick the secret number."""
    points: int = 0
    greet(player)
    hint()
    points += 2
    while guess(x) != secret:
        guess(x)
        points += 1
    else:
        return guess(x)

def guess(z: int) -> int:
    """Defined the guess function for the game, which allows players to make multiple guesses for the secret number."""
    print(f"Now {player}, make your next integer guess (+1 stroke): ")
    z: int = int(input())
    if z < secret:
        print("Not quite. Guess a higher number.")
    if z > secret:
        print("Not quite. Guess a lower number.")
    if z == secret:
        print(f"You got it! Congratulations! Your total strokes were ")
        quit()


def hint() -> None:
    """Defined a hint function for the game that allows the player an option to take a hint as their second turn."""
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    print(f"{player}, you have the option of taking another hint (+2 strokes). The hint will tell you if the secret number is even (green) or odd (yellow). If you would like to take the hint, input a 'y' now. ")
    answer: str = input()
    if answer == "y":
        if secret % 2 == 0:
            print(GREEN_BOX)
        else:
            print(YELLOW_BOX)
    else:
        return


if __name__ == "__main__":
    main()