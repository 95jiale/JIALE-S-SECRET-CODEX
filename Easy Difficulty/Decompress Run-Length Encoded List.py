from itertools import repeat


def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    theList = []
    for i in range(int(len(nums)/2)):
        freq = nums[2*i]
        val = nums[2*i+1]
        #print([nums[2*i], nums[2*i+1]])
        theList.extend(repeat(val, freq))
    print(theList)


answer = decompressRLElist([1, 2, 3, 4])
print(answer)
