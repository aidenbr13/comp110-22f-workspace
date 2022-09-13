"""EX03 - Wordle"""

__author__: str = "730320104"

def contains_char(word: str, character: str) -> str:
    """Defining a function that tests if a character is found in a given word"""
    assert len(character) == 1
    i: int = 0
    while i < len(word):
        if character == word[i]:
            return True
        else:
            i= i + 1
    return False

def emojified(predict: str, secret: str) -> str:
    """Defining a function that prints emojis that correlate to the characters of a guess in relation to a secret word"""
    assert len(predict) == len(secret)
    i: int = 0
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji = ''
    while i < len(secret):
        if predict[i] == secret[i]:
            i= i + 1
            emoji += green_box
        else:
            if contains_char(secret, predict[i]) == True:
                emoji += yellow_box
            else:
                emoji += white_box
            i= i + 1
    return emoji

def input_guess(length: int) -> int:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    else:
        return(guess)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    n: int= 1
    print(f"=== Turn {n}/6 ===")
    wordle: str = "codes"
    guessing: str = input_guess(5)
    while n < 6:
        if guessing == wordle:
            print(emojified(guessing, wordle))
            print(f"You won in {n}/6 turns!")
            return
        if guessing != wordle:
            print(emojified(guessing, wordle))
            n= n + 1
            print(f"=== Turn {n}/6 ===")
            guessing = input_guess(5)
    print(emojified(guessing, wordle))
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()