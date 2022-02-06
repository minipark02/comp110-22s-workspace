"""Structured Wordle with Turns and Functions."""

__author__ = "730388033"


def contains_char(search_str: str, one_char: str) -> bool:
    """When entering a str, you can search for a single character inside."""
    assert len(one_char) == 1
    char_index: int = 0
    while char_index < len(search_str):
        if search_str[char_index] == one_char[0]:
            return True
        else:
            char_index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Associates specific coloured emoji box with contains_char function."""
    assert len(guess) == len(secret)
    guess_index: int = 0
    emoji_guess: str = ""
    guess_char: bool = False
    while guess_index < len(secret):
        if guess[guess_index] == secret[guess_index]:
            emoji_guess += GREEN_BOX
        else:
            guess_char = contains_char(secret, guess[guess_index])
            if guess_char:  
                emoji_guess += YELLOW_BOX
            else:
                emoji_guess += WHITE_BOX
        guess_index += 1
    return emoji_guess


def input_guess(expected_len: int) -> str:
    """When given an expected length of a guess, it should return the guess back with the appropriate length."""
    guess = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:
        guess: str = input(f"That was not {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    win: bool = False
    secret: str = "codes"
    input_guess = len(secret)
    while turns <= 6 and win is not True:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input(f"Enter a {input_guess} character word: ")
        print(emojified(guess, secret))
        if guess == secret:
            win = True
        else:
            turns += 1
    if win is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    turns = 0
    

if __name__ == "__main__":
    main()