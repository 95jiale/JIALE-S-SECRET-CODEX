def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    #count = 0
    theList = []
    for x in nums:
        count = 0
        for y in nums:
            if x > y:
                count = count + 1
        theList.append(count)
        #count = 0
    print(theList)


answer = smallerNumbersThanCurrent([6, 5, 4, 8])
print(answer)
