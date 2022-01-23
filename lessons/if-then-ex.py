"""Practice with if-then-else statements."""

choice: int = int(input("Enter a number please: "))

if choice < 75:
    print("A")
else:
    if choice < 80:
        print("B")
    else:
        if choice < 95:
            print("C")
        else:
            print("D")
print("Game over. Thank you for playing.")