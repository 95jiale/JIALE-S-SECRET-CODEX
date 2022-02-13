# Looping numbers
# Default value for start = 0, Default value for step = 1
for i in range(10):
    print(i)  # Prints i from 0 to 9

# (start,stop)
for i in range(1, 9):
    print(i)  # Prints i from 1 to 8

# (start, stop, step)
for i in range(2, 15, 2):
    print(i)  # Prints i from 2 to 14

for i in range(5, 1, -1):
    print(i)  # Prints i from 5 to 2

# Looping through list/array/tuple
theList = [2, 56, "Hello", [2, 3]]

# Loop through elements in the list
for element in theList:
    print(element)


# Loop through index of a list
nums = [5, 4, 3, 2, 1]
for i in range(len(nums)):  # len(nums) = 5 > range is 0,1,2,3,4
    print(i)  # index of list > 0,1,2,3,4
    print(nums[i])  # value of list > 5,4,3,2,1


# Loop through a string
theString = "Hello World!"
for character in theString:
    print(character)

for i in range(len(theString)):
    print(i)  # index
    print(theString[i])  # character


# counter loops
    count = 0
    for x in range(len(nums)):
        count = count + 1
    return count


# a FULL loop
    for x in range(len(nums)):
        for y in range(len(nums)):
            print([x, y])

# joins a list of string into a single string
theString = ""
newList = ['l', 'e', 's', 'i', 'k']
print(theString.join(newList))  # "lesik"

# variables
x = 8

# functions


def multiply(nums)


# elements
(a, b, c, d, e)

# arguments/parameters
things we put inside a function e.g nums > def multiply(nums)

# type
float, integer, boolean, tuple, string, list, array, set*

# replace function
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)


# slicing a string function ONLY STRING
[a:b]
a is where you start slicing(inclusive)
b is where you slicing(exclusive)

# sort the value inside the bracket  e.g theArray = [(y,2), (z,3), (x,1)] > [(x,1),(y,2),(z,3)]
theArray.sort(key=lambda x: x[1])

# intersection function to compare common factor in a SET ONLY
edges = [[1, 2], [2, 3], [4, 2]]
valNode = set.intersection(set(edges[0]), set(edges[1]))

FOR LOOPS

IF/else OR IF/ELIF

DOUBLE FOR LOOPS > 2 inputs

int(), str(), float() > function

range(start, stop, step)


["is", "1", "ma", "!@#"]
index[1] = "1"
position 1 = "is"
