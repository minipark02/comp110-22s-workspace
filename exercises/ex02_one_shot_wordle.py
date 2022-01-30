"""Ex02 - Another step toward making Wordle."""

__author__ = "730388033"

secret: str = "python"

guess: str = input("What is your 6-letter guess? ")

while len(guess) < len(secret) or len(guess) > len(secret):
    guess: str = input("That was not 6 letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess_index: int = 0
emoji_guess: str = ""
possible_character: bool = False
alternative_index: int = 0

while guess_index < len(secret):
    if guess[guess_index] == secret[guess_index]:
        emoji_guess += GREEN_BOX
    else:
        while possible_character is not True and alternative_index < len(secret):
            if guess[guess_index] == secret[alternative_index]:
                possible_character = True
            else:
                alternative_index += 1
        if possible_character is True:
            emoji_guess += YELLOW_BOX
        else:
            emoji_guess += WHITE_BOX
    guess_index += 1
    possible_character = False
    alternative_index = 0
print(emoji_guess)

if guess != secret:
    print("Not quite. Play again soon!")
elif guess == secret:
    print("Woo! You got it!")