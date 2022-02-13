def subtractProductAndSum(n):
    """
    :type n: int
    :rtype: int
    """
    theProduct = 1
    theSum = 0
    for x in str(n):
        theSum = int(x) + theSum
        theProduct = int(x)*theProduct
    #theResult = theProduct - theSum
    print(theProduct - theSum)


answer = subtractProductAndSum(4421)
print(answer)
