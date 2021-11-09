def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    newList = [1] * len(s)
    theString = ""
    for i in range(len(s)):
        #print(s[i] , indices[i])
        newList[indices[i]] = s[i]
    # joins a list of string into a single string
    print(theString.join(newList))


answer = restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
print(answer)

# newList [1,1,1,1,1replace(c),1,1,1]
#newList[4] = "c"
# replace into
#newList[indices[i]] = s[i]
