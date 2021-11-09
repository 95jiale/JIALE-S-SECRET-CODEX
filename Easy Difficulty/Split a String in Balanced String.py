def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    Rnum = 0
    Lnum = 0
    balance = 0

    for i in s:
        if i == "L":
            Lnum = Lnum + 1
        elif i == "R":
            Rnum = Rnum + 1
        if Lnum == Rnum:
            balance = balance + 1
            Lnum = 0
            Rnum = 0
    print(balance)


answer = balancedStringSplit("LLLLRRRR")
print(answer)
