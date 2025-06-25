#Q1. Create a dictionary for a book with 2 properties.Access a specific value.Add a new key-value pair.
#delete one key.Loop through and print all key-value pairs.
#ans:
book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    }
print(book.get("title"))
book.update({"year": str(2020)})
print(book.items())
book.pop("title")
for key, value in book.items():
    print(key, value)

#q2. Use indexing and slicing on a string.Print the first and last character.Print every second character.
# Print the reversed string.
# ans:

name = "harika"
print(name[0])
print(name[-1])
print(name[::-1])

#q3. Write a function that accepts a name and returns a welcome message.
#ans:

def welcome(name):
    print("welcome" + name)

name = input("Enter your name: ")
welcome(name)

#Q4. Write a function that takes a number and returns its cube.
#ans:
num= input("Enter a number: ")
num = int(num)

def cube(num):
   return num * num * num

print(cube(num))

#Q5. Use a nested function call involving at least 3 built-in functions.
# Add a comment explaining which one runs first.
#ans:

num= input("Enter a number:"" ")
num = float(num)

def fun(num):
    num = int(abs(round(num)))
    return num

print(fun(num))

# Q6. Create a function with two parameters and call it using keyword arguments.
#ans:
name= input("Enter a name:")
age = input("Enter age:")
age = str(age)

def fun(name,age):
    return name + " is " + age + " years old"

print(fun(name,age))

# Q7. Write a function that accepts any number of scores and returns the average using *args.
#ans:

def fun(*args):
    total = 0
    for arg in args:
        total += arg
    average = total / len(args)
    return average

print(fun(4,2))

# Q8. Create a variable outside a function.Create a function with the same variable name inside.
#Print both values and explain the difference in scope using comments
#ans:

name = "harika"

def fun():
    name = "anvil"
    print(name)

print(fun())
print(name)
#explaination: the variable inside function is considered only when the function is called otherwise it prints the
# variable outside the function

