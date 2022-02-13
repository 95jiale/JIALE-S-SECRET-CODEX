def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """
    valNode = 0
    # for x in range(0, len(edges)-1, 1):
    # print(edges[x])
    # we just want to compare ONLY the first and second element inside edges therefore no need to loop
    valNode = set.intersection(set(edges[0]), set(edges[1]))

    print(list(valNode)[0])

    for x in edges[0]:
        if x in edges[1]:
            print(x)


answer = findCenter(edges=[[1, 2], [2, 3], [4, 2]])
print(answer)
