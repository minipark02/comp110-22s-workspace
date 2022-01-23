"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it? ")
guess: int = int(input("What's your guess? "))

if guess == SECRET: 
    print("You guessed correctly! Great job!!")
    print("Have a wonderful day!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high! Try again!")
    else:
        print("You guessed too low! Try again!")

print("Game over.")