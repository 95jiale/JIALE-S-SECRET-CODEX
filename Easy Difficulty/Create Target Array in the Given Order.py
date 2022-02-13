def createTargetArray(nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    theArray = []
    for x in range(len(nums)):
        theArray.insert(index[x], nums[x])
    print(theArray)


answer = createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
print(answer)
