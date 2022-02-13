def interpret(command):
    """
    :type command: str
    :rtype: str
    """
    theString = ""
    while len(command) > 0:
        if command.startswith("G"):
            theString = theString + "G"
            command = command.replace("G", "", 1)
        elif command.startswith("()"):
            theString = theString + "o"
            command = command.replace("()", "", 1)
        elif command.startswith("al"):
            theString = theString + "al"
            command = command.replace("(al)", "", 1)
    print(theString)

    # command = command.replace("()", "o").replace("(al)", "al")
    # print(command)


answer = interpret("G()(al)")
print(answer)
