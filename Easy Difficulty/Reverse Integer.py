class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #x = 123
        # 1 convert x into a string: str(x) Output: "123"
        # 2 for loop -> loops through the str and print the individual digits
        # 3 convert digits back into a integer using int(digit)
        # 4 add digits into theList

        theList = []
        if x < 0:
            y = x * (-1)
        else:
            y = x
        for digit in str(y):
            theList.append(int(digit))  # adds digit into theList

        theList.reverse()  # reversed the list already

        output = ""  # making a new str group to print
        for digit1 in theList:
            output = output + str(digit1)  # adding str with a str

        if x < 0:  # input is negative
            output = int(output) * (-1)
            if int(output) < -2**31:  # constraint
                return 0
            else:
                return int(output)

        else:  # input is positive and zero 0
            if int(output) > 2**31-1:  # constraint
                return 0
            else:
                return int(output)
