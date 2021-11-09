def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    maxCandies = 0
    theList = []
    for x in candies:
        if x > maxCandies:
            maxCandies = x
    # maxCandies now is = 5 #solved for the highest candies a kid has
    print("Max candies is:  " + str(maxCandies))

    for i in candies:
        i = i + extraCandies
        if i >= maxCandies:
            theList.append(True)
        else:
            theList.append(False)
    print(theList)


answer = kidsWithCandies([12, 1, 12], 10)
print(answer)
