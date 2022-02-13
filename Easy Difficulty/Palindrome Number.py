class Solution(object):
    def isPalindrome(self, x):  # defining the function
        """
            :type x: int
            :rtype: bool
        """
        reversestring = str(x)[::-1]  # reversing a str command

        if reversestring == str(x):
            return True

        elif x < 0:
            return False

        else:
            return False

    # printing the definition with the input digits allocated
    # print(isPalindrome())
    # what we want to see
