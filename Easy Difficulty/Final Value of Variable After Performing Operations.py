def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    X = 0

    for y in operations:
        if y == "--X" or y == "X--":
            X = X - 1
        elif y == "++X" or y == "X++":
            X = X + 1
    return X


# this returns the function and what the system runs
answer = finalValueAfterOperations(["++X", "++X", "X++"])
print(answer)
