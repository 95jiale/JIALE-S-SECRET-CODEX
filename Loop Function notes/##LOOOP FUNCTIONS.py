# LOOOP FUNCTIONS


# loop numbers

# default start is 0 step is 1
for i in range(10):
    print(i)  # this will output will print i from 0 to 9

for i in range(1, 9):  # 1 is start, 9 is stop, step is default 1
    print(i)  # this will output print i from 1 to 8


for i in range(2, 15, 2):  # 2 start,15 stop,step  of 2
    print(i)  # prints 2 to 14

for i in range(5, 1, -1):  # reverse way from 5 to 2
    print(i)


# loop through (list/array/tuple)
theList = [2, 56, "Hello", [2, 3]]

# loop through element in the list
for element in theList:
    print(element)  # [2,56,"Hello",[2,3]]

# loop through index of a list (string/INTEGER)
for i in range(len(theList)):
    print(i)  # index of list
    print(theList(i))  # element of list in side theList

# loop through a string
theString = "Hello World!"
for character in theString:
    print(character)


# loop through an index or a characters
for i in range(len(theString)):
    print(i)  # print out the index
    print(theString[i])  # print out the character/element
