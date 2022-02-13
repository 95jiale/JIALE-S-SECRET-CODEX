def sumOddLengthSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    theSum = 0
    for x in range(1, len(arr)+1, 2):
        numLoop = len(arr)-x+1
        print(x)
        print(numLoop)
        # x = 1 , 3 , 5
        # numLoop =5 , 3, 1
        for y in range(numLoop):
            theSum += sum(arr[y:y+x])
    print(theSum)


answer = sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3])
print(answer)


# x=1 loop 5
# x=3 loop 3
# x=5 loop 1
