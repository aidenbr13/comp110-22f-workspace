"""EX06 - Choose your own adventure."""

__author__: str = "730320104"

from random import randint

secret: int = randint(1,100)

x: int = 0

player: str = ""

points: int = 0

keep_playing: int = 0


def greet() -> None:
    """Defined a function that greets a player when joining the game and helps them understand their first decision."""
    global points
    global player
    print("Hi, and welcome to NUMBER GOLF, the game show where you guess a randomly generated integer between 1 and 100 in the least amount of attempts. The goal of the game is to correctly guess the number and have the least amount of strokes. What is your name, contestant? ") 
    player = input()
    print(f"Ok {player}, let's begin the game! You have 3 options for your first 'shot': a) guess a random integer (+1 stroke), b) ask for a hint (+2 strokes), or c) give up (+1000 strokes). Please type your selection now: (a/b/c) ")
    y: str = input()
    if y == "a":
        f = int(input("What is your integer guess? "))
        if f < secret:
            print("Not quite. Guess a higher number.")
            points += 1
        if f > secret:
            print("Not quite. Guess a lower number.")
            points += 1
        if f == secret:
            print(f"Hole in one! Congratulations!")
            points = 10
    if y == "b":
        points = points + 2
        if secret <= 50:
            print("The secret number is less than or equal to 50.")
        else:
            print("The secret number is greater than 50.")
    if y == "c":
        points = points + 1000
        print(f"Thank you for playing. Your total strokes was {points}.")
        points = 10


def guess(z: int) -> int:
    """Defined the guess function for the game, which allows players to make multiple guesses for the secret number."""
    global points
    global player
    global keep_playing
    print(f"Now {player}, make your next integer guess (+1 stroke): ")
    z: int = int(input())
    if z < secret:
        points += 1
        print("Not quite. Guess a higher number.")
    if z > secret:
        points += 1
        print("Not quite. Guess a lower number.")
    if z == secret:
        print(f"You got it! Congratulations! Your total strokes were {points}.")
        points = 10


def hint() -> None:
    """Defined a hint function for the game that allows the player an option to take a hint as their second turn."""
    global points
    global player
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    print(f"{player}, you have the option of taking another hint (+2 strokes). The hint will tell you if the secret number is even (green) or odd (yellow). If you would like to take the hint, input a 'y' now. ")
    answer: str = input()
    if answer == "y":
        points += 2
        if secret % 2 == 0:
            print(GREEN_BOX)
        else:
            print(YELLOW_BOX)
    else:
        return


def main() -> None:
    """Defined the 'main' function of our game that runs and lets the player try to pick the secret number."""
    global points
    global player
    global keep_playing
    while keep_playing == 0:
        greet()
        while points < 2:
            hint()
        while points < 10:
            guess(x)
        input(f"{player}, great job. Would you like to play again? Input the 'y' and 'ENTER' keys twice if yes and the 'n' and 'ENTER' keys twice if no: ")
        points = 0
        if input() == "n":
            keep_playing = 1


if __name__ == "__main__":
    main()