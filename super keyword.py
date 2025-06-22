class rose():
    def __init__(self):
        print("Rose")
    def display(self):
        print("Rose is live")
class jack():
    def __init__(self):
        print("Jack")
    def display(self):
        print("Jack is alive")
class titanic(jack,rose):
    def __init__(self):
        super().__init__()
        print("Titanic ship")
    def display(self):
        print("Titanic ship is broken")
obj1=titanic()
obj1.display()
