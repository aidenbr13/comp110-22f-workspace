"""EX02 - One Shot Wordle."""

__author__: str = "730320104"

word: str = "python"

length: int = len(word)

guess: str = input(f"What is your {length}-letter guess? ")

i: int = 0

white_box: str = "\U00002B1C"

green_box: str = "\U0001F7E9"

yellow_box: str = "\U0001F7E8"

"""Create an output for an instance in which the player does not guess a word with the desired number of characters"""

while len(guess) != len(word):
    print(f"That was not {length} letters! Try again: ", end='')
    guess: str = input()

else:
    if guess != word:
        while i < len(word):
            if guess[i] == word[i]:
                print(green_box, end='')
                """Created an output for if the character of the guessed word was in the same index as the secret word"""
            if guess[i] != word[i]:
                if guess[i] in word:
                    print(yellow_box, end='')
                    """Created an output for if a character of the guessed word appears in the secret word, but not at the same index"""
                else: 
                    print(white_box, end='')
                """Created an output for if a character in the guessed word does not appear in the secret word"""
            i = i + 1
        print("\nNot quite. Play again soon!")
    if guess == word:
        while i < len(word):
            if guess[i] == word[i]:
                print(green_box, end='')
            i = i + 1
        print("\nWoo! You got it!")
        """Created an output for if the guessed word was the same as the secret word; the player wins the game"""