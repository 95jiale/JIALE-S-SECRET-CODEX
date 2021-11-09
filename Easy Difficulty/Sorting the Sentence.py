def sortSentence(s):
    """
    :type s: str
    :rtype: str
    """
    theList = ""
    theArray = s.split()
    for x in range(len(theArray)):
        # print(s.split()[x])
        #print((theArray[x][:-1], theArray[x][-1:]))
        theArray[x] = ((theArray[x][:-1], theArray[x][-1:]))
        print(theArray[x])
    theArray.sort(key=lambda x: x[1])
    print(theArray)
    for y in range(len(theArray)):
        theList = theList + (theArray[y][0]) + " "
    print(theList[:-1])


answer = sortSentence(s="is2 sentence4 This1 a3")
print(answer)
