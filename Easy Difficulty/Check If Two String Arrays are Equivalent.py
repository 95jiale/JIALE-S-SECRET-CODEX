def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    theArray1 = ''
    theArray2 = ''
    for i in range(len(word1)):
        theArray1 += word1[i]
    for j in range(len(word2)):
        theArray2 += word2[j]
    return theArray1 == theArray2
    # #if theArray1 == theArray2:
    #     print(True)
    # else:
    #     print(False)


# alternatively
# return '',join(word1) == ''.join(word2)
answer = arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"])
print(answer)
