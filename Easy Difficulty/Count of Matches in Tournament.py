def numberOfMatches(n):
    """
    :type n: int
    :rtype: int
    """
    teamAdvanced = n
    totalMatches = 0

    while teamAdvanced != 1:
        if teamAdvanced % 2 == 0:
            totalMatches += teamAdvanced/2  # 0 + 3.5 = 3.5
            teamAdvanced = teamAdvanced/2  # 3.5
        elif teamAdvanced % 2 == 1:
            totalMatches += (teamAdvanced-1)/2
            teamAdvanced = (teamAdvanced-1)/2 + 1

    print(totalMatches)


answer = numberOfMatches(n=14)
print(answer)
