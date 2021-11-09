def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    maxWealth = 0
    for x in accounts:
        if sum(x) > maxWealth:
            # replace sum(x) into maxWealth, it will loop until the largest and then return
            maxWealth = sum(x)
    return maxWealth


answer = maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
print(answer)
