def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    brackets = ""
    for x in address:
        if x == ".":
            # brackets + "[.]"  can just + a string with a string
            brackets += "[.]"
        else:
            brackets += x
    return brackets
# msg += "three falcons"  >>  msg = msg + "three falcons"

# ALTERNATIVELY brackets.append("[.]") can also append this into the list


answer = defangIPaddr("1.1.1.1")
print(answer)
#output is "1,[.],1,[.],1,[.],1"


def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    brackets = []
    for x in address:
        if x == ".":
            brackets.append("[.]")
        else:
            brackets.append(x)
    return "".join(brackets)


answer = defangIPaddr("1.1.1.1")
print(answer)

# ALSOOOOO >>> return address.replace("." , "[.]")
