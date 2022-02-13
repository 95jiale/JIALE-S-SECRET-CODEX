def checkIfPangram(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    theList = []
    for i in range(len(sentence)):
        if sentence[i] not in theList:
            theList.append(sentence[i])
    if len(theList) == 26:
        return True
    else:
        return False


answer = checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog")
print(answer)
