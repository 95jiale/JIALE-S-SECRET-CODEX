def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    theList = []
    for x in range(n):  # loop through an INTEGER of a list  x will start from 0 end at n-1 and the step is 1
        theList.append(nums[x])  # append the element of the index x into list
        # append the element of the index (x + n) into list
        theList.append(nums[x+n])
    print(theList)

    # print(nums[2])  #print the element of the index


answer = shuffle([2, 5, 1, 3, 4, 7], n=3)
print(answer)
