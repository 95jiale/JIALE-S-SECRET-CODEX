class ParkingSystem(object):
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big  # properties
        self.medium = medium  # properties
        self.small = small  # properties

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool True/False
        """
        # if its a Big car
        if carType == 1:
            # check if ParkingSystem Big has space
            if self.big >= 1:
                self.big = self.big - 1  # 1 Big space is occupied
                return True
            else:  # no Big space
                return False
        # if its a Medium car
        elif carType == 2:
            # check if ParkingSystem Medium has space
            if self.medium >= 1:
                self.medium = self.medium - 1  # 1 Medium space is occupied
                return True
            else:  # no Medium space
                return False
        # if its a Small car
        elif carType == 3:
            # check if ParkingSystem Small has space
            if self.small >= 1:
                self.small = self.small - 1  # 1 Small space is occupied
                return True
            else:  # no Small space
                return False


#1 - big
#2 - medium
#3 - small


obj = ParkingSystem(1, 1, 0)
print(ParkingSystem(1, 1, 0))
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
