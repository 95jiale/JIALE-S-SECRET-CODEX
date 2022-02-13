def maxDepth(s):
    """
    :type s: str
    :rtype: int
    """
    leftB = 0
    depth = 0
    for x in range(0, len(s), 1):
        if "(" == s[x]:
            leftB += 1
            if leftB > depth:
                depth = leftB
        elif ")" == s[x]:
            leftB -= 1
    print(depth)


answer = maxDepth(s="(1)+((2))+(((3)))")
print(answer)
