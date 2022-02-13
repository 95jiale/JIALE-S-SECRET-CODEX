def length(nums):
    count = 0
    for x in range(len(nums)):
        count = count + 1
    return count


answer = length([1, 5, 8, 1, 5, 7, 23, 34])
print(answer)
