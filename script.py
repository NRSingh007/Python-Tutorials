# -------------------PYTHON TUTORIAS-------------------------------

# simple print statement (string)
print("To be printed inside the quotation")

# ----------------------------------------------------------------

# storing value(string) in a variable
variableName = "Any statement to be printed"
print(variableName)

# ----------------------------------------------------------------

# storing value(numbers) in a variable
varName = 123456
print(varName)

# ----------------------------------------------------------------

# taking input
var_name = input("Enter any: ")
print("You have entered", var_name)

# ----------------------------------------------------------------

# taking input with specific dataTypes
var_number = int(input("Enter number: "))
print("You have entered", var_number)

# ----------------------------------------------------------------

# concat => joining variables
first_name = "JAMES"
last_name = "BOND"
age = 35

full_name = first_name + " " + last_name

details = full_name + " " + str(age)

print(full_name)
print(details)

# ----------------------------------------------------------------

# "if", "else" condition
a = 2       # assigning values to variable
b = 5

if a < b:
    print("a is smaller than b")
else:
    print("a is greater than b")

# ----------------------------------------------------------------

# "if", "elif", "else" condition
x = 10
y = 15
z = 10

if x == y:
    print("x has same value as y")
elif x == z:
    print("x has same value as z")
else:
    print("Value of x is not similar to any of the remaining value")

# ----------------------------------------------------------------

# list => A list is a collection which is ordered and changeable. In Python lists are written with square brackets, similar to array(collection of similar data types elements)
new_list = [1, 2, "red", "yellow", "green"]
print(new_list)

for i in new_list:
    print(i)

# ----------------------------------------------------------------

# Tuple => A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

# You can access tuple items by referring to the index number, inside square brackets:
print(this_tuple[1])

# ----------------------------------------------------------------

# Sets => A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
this_set = {"apple", "banana", "cherry"}
print(this_set)

# Check if "banana" is present in the set:
print("banana" in this_set)

# ----------------------------------------------------------------

# dictionaries => A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict)

for key, value in this_dict.items():
    print(key, ":", value)

# ----------------------------------------------------------------

# while loop
i = 1
while i < 6:
    print(i)
    i += 1

# break Statement => With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# ----------------------------------------------------------------

# for loop

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)

# Nested Loops

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# ----------------------------------------------------------------