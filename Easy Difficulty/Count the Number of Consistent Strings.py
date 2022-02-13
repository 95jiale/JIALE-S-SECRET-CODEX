def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    count = 0
    # for word in words:
    #     consistent = True
    #     for char in word:
    #         if char not in allowed:
    #             consistent = False
    #             break
    #     if consistent:
    #         count += 1
    # print(count)
    # ALTERNATIVELY~~~~~~~

    for word in words:
        consistent = 0
        for char in word:
            if char in allowed:
                consistent += 1
        if consistent == len(word):
            count += 1
    print(count)


answer = countConsistentStrings(
    allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
print(answer)
