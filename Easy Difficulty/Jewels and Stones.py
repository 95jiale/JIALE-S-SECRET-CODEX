def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    count = 0
    for x in stones:
        if x in jewels:
            count = count + 1
    print(count)


answer = numJewelsInStones("z", "ZZ")
print(answer)
