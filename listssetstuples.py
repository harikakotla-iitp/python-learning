# Q1. Create a list of 5 of your favorite movies.Print the first, last, and middle movie using indexing.
#Reverse the list using slicing.
#answer:

movies = ["a", "b", "c","d","e"]
print(movies[0])
print(movies[2])
print(movies[-1])
print(movies[::-1])

#Q2. Create a list of numbers from 10 to 100 with a step of 10.Print all even-positioned elements using slicing (i.e., 2nd, 4th...)
#Print the list in reverse order
#ans:
numbers = list(range(10,101,10))
print(numbers[::2])
print(numbers[::-1])

# Q3. Create a tuple of 4 fruits.Print the second fruit.Try to change one item → What error do you get?
#ans:
fruit= ("apple", "banana", "cherry","orange")
print(fruit[1])
#fruit[0] = "kiwi"
#error: Traceback (most recent call last):
#  File "C:\Users\kotla\PycharmProjects\PythonProject\listssetstuples.py", line 22, in <module>
  #  fruit[0] = "kiwi"

#TypeError: 'tuple' object does not support item assignment

# Q4. Use slicing on the tuple to get only the middle two fruits
#ans:
print(fruit[1:3])

#Q5. Create a set of 5 random colors (including duplicates).Print the set (notice duplicates get removed).Add one more color.Remove a colorCheck if "red" is in the set
#ans:
colors = {"red", "green", "blue", "yellow","yellow"}
print(colors)
colors.add("pink")
print(colors)
colors.remove("green")
print(colors)
if "red" in colors:
    print("Red is in the set!")
else:
    print("Red is not in the set.")

#output:
# {'red', 'blue', 'green', 'yellow'}
#{'red', 'blue', 'yellow', 'green', 'pink'}
#{'red', 'blue', 'yellow', 'pink'}
#Red is in the set!

#Q6. Bonus: From a string "Harika", print:First letter,Last letter,Reverse it using slicing
#ans:
name = "harika"
print(name[0])
print(name[-1])
print(name[::-1])
