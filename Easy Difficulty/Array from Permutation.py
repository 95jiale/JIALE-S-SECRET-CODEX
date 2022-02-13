nums = [5, 0, 1, 2, 3, 4]

newArray = []  # create an empty list
for x in range(len(nums)):  # loop through every digit in the list
    newArray.append(nums[nums[x]])
print(newArray) # prints new array
