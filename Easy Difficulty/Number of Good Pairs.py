def numIdenticalPairs(nums):
    """
        :type nums: List[int]
        :rtype: int
        """
    count = 0
    # -1 is to eliminate the last loop to compare last number as x and no number for y
    for x in range(len(nums)-1):
        for y in range(x+1, len(nums)):  # condition to loop from starting and ending point
            if nums[x] == nums[y]:  # also can use and x < y
                count = count + 1
    print(count)


answer = numIdenticalPairs([1, 2, 3, 1, 1, 3])
print(answer)
