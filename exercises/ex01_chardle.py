"""Ex01 - Chardle - A cute step toward Wordle."""

__author__ = "730388033"

word: str = str(input("Enter a 5-character word: "))
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
char: str = str(input("Enter a single character: "))
if len(char) < 1:
    print("Error: Character must be a single character. ")
    exit()
if len(char) > 1:
    print("Error: Character must be a single character. ")
    exit()
print("Searching for " + char + " in " + word)

if char == word[0]:
    print(char + " found at index 0")
if char == word[1]:
    print(char + " found at index 1")
if char == word[2]:
    print(char + " found at index 2")
if char == word[3]:
    print(char + " found at index 3")
if char == word[4]:
    print(char + " found at index 4")

match: int = word.count(char)

if match == 0:
    print("No instances of " + char + " found in " + word)
else:
    if match == 1:
        print("1 instance of " + char + " found in " + word)
        if match == 2:
            print("2 instances of " + char + " found in " + word)
            if match == 3:
                print("3 instances of " + char + " found in " + word)
                if match == 4:
                    print("4 instances of " + char + " found in " + word)
                    if match == 5:
                        print("5 instances of " + char + " found in " + word)