class Person:
    def __init__(self, name, age, state):
        self.name = name
        self.age = age
        self.state = state

    def goToSleep(self):
        if self.state == "awake":
            print("going to sleep!")
            self.state = "sleep"
        else:
            print("I am already asleep")

	
# WHat a class has is properties
# all the things in self.<> are properties of this class

# def in the class is a method/function in the class


p1 = Person("John", 36,"awake")

p2 = Person("Jun Hao",18,"sleep")

p1.goToSleep()
print(p1.state)

p2.goToSleep()