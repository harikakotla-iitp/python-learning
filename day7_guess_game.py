from random import randint

x = randint(1, 100)
guesses = 0

while guesses < 5:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1
        if guess == x:
            print("You guessed right!")
            break
        elif guess < x:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("That's not a number!")

else:
    print("Out of guesses!")
    print("The correct number was", x)

print("Thanks for playing!")
