#Q1.Create a function that accepts any number of keyword arguments and prints them.
#ans:
def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

fun(name='harika', age=18)

#Q2. Use .format() to create a string that says:
#"User Alice has logged in from device Mobile"
#ans:

name = "alice"
item = "mobile"

print("user {} has logged in from device {}".format(name, item))

# Q3. Write a program that:
#Generates a random number between 1 and 50

#Asks the user to guess it (you can use a variable like guess = 20 instead of input)

#Tells the user if their guess was correct or not
#ans:

import random

guess = input("guess a number between 1 and 50: ")
guess = int(guess)
print(random.randint(1,50))
if guess == item:
    print("you guessed right")
else :
    print("you guessed wrong")

#Q4. Create a list of 5 cities and randomly select one using random.choice()
#ans:

list = ["bombay","newyork","hyderabad","delhi","kolkata"]
print(random.choice(list))

#Q5. Write code that:Asks the user to divide two numbers (use hardcoded values).Wraps the division inside
#try-except Handles ZeroDivisionError and prints a message

try:
    numerator = int(input("enter a number(num): "))
    denominator =int(input("enter another number(den): "))
    result= numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero")
except Exception as e:
    print(e)
    print("something went wrong")

# Q6.Try to shuffle a list of colors using random.shuffle() and print it before and after shuffling.
#ans:

colours = ["red","blue","green","yellow","pink"]
print(colours)
random.shuffle(colours)
print(colours)