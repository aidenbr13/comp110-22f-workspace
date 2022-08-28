"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730320104"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

guess: str = input("Enter a single character: ")

if len(guess) !=1:
    print("Character must be a single character.")
    exit()

print("searching for " + guess + " in " + word)

count: int = 0

if guess == word[0]:
    count = count + 1
    print(guess + " found at index 0"); 

if guess == word[1]:
    count = count + 1
    print(guess + " found at index 1"); 

if guess == word[2]:
    count = count + 1
    print(guess + " found at index 2"); 

if guess == word[3]:
    count = count + 1
    print(guess + " found at index 3"); 

if guess == word[4]:
    count = count + 1
    print(guess + " found at index 4"); 

if count == 1:
    print("1 instance of " + guess + " found in " + word)

if count == 0:
    print("No instances of " + guess + " found in " + word)

if count == 2:
    print("2 instances of " + guess + " found in " + word)

if count == 3:
    print("3 instances of " + guess + " found in " + word)

if count == 4:
    print("4 instances of " + guess + " found in " + word)

if count == 5:
    print("5 instances of " + guess + " found in " + word)