# rmb to take out self before solving
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    addition = 0
    theList = []
    for x in (nums):
        addition = x + addition
        theList.append(addition)
    return theList


answer = runningSum([3, 1, 2, 10, 1])
print(answer)
