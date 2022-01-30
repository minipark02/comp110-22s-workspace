"""Ex02 - Another step toward making Wordle."""

__author__ = "730388033"

SECRET: str = "python"

guess: str = input("What is your 6-letter guess? ")

while len(guess) < len(SECRET):
    guess: str = input("That was not 6 letters! Try again: ")
    if len(guess) > len(SECRET):
        guess: str = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_index: str = guess[0]
emoji_guess: str = ""

while guess_index < SECRET[len(SECRET) - 1]:
    if guess_index == SECRET[0]:
        emoji_guess += GREEN_BOX
    elif guess_index == SECRET[1]:
        emoji_guess += GREEN_BOX
    elif guess_index == SECRET[2]:
        emoji_guess += GREEN_BOX
    elif guess_index == SECRET[3]:
        emoji_guess += GREEN_BOX
    elif guess_index == SECRET[4]:
        emoji_guess += GREEN_BOX
    elif guess_index == SECRET[5]:
        emoji_guess += GREEN_BOX
    else:
        emoji_guess += WHITE_BOX
    guess_index: str = guess[0 + 1]   
print(emoji_guess)

if guess != SECRET:
    print("Not quite. Play again soon!")
elif guess == SECRET:
    print("Woo! You got it!")