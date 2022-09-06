"""EX02 - One Shot Wordle."""

__author__: str= "730320104"

word: str = "knoll"

length: str = len(word)

guess: str = input(f"What is your {length}-letter guess? ")

i: int = 0

WHITE_BOX: str = "\U00002B1C"

GREEN_BOX: str = "\U0001F7E9"

YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(word):
    print(f"That was not {length} letters! Try again:", end = ' ')
    guess: str = input()

else: 
    if guess != word:
        while i<len(word):
            if guess[i]==word[i]:
                print(GREEN_BOX, end = '')
                i = i + 1
            if guess[i] != word[i]:
                if guess[i] in word:
                    print(YELLOW_BOX, end ='')
                else: print (WHITE_BOX, end ='')
                i = i + 1
        print("\nNot quite. Play again soon!")
    if guess == word:
        while i<len(word):
            if guess[i]==word[i]:
                print(GREEN_BOX, end ='')
            i = i + 1
        print("\nWoo! You got it!")