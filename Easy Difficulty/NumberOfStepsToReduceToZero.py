def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0

    while num != 0:
        if num % 2 == 0:
            num = num/2
            steps = steps + 1
        elif num % 2 == 1:
            num = num - 1
            steps = steps + 1
    print(steps)


answer = numberOfSteps(14)
print(answer)
