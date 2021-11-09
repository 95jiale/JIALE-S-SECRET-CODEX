def countMatches(items, ruleKey, ruleValue):
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """
    count = 0
    indexVar = 0
    if ruleKey == "type":
        indexVar = 0
    elif ruleKey == "color":
        indexVar = 1
    elif ruleKey == "name":
        indexVar = 2

    for x in range(len(items)):
        if ruleValue == items[x][indexVar]:
            count = count + 1
    print(count)


answer = countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], [
                      "phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone")
print(answer)
