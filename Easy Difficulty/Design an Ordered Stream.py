class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.store = [None] * n  # a list
        self.pointer = 0  # a number

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        theList = []
        self.store[idKey-1] = value

        while self.store[self.pointer] != None and self.pointer < (len(self.store)):
            theList.append(self.store[self.pointer])
            self.pointer = self.pointer + 1
        print(theList)


os = OrderedStream(5)
os.insert(3, "ccccc")
os.insert(1, "aaaaa")
os.insert(2, "bbbbb")
os.insert(5, "eeeee")
os.insert(4, "ddddd")


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
