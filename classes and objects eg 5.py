class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def display(self):
        print("add",self.num1+self.num2)
        print("sub",self.num1-self.num2)
        print("mul",self.num1*self.num2)
        print("div",self.num1/self.num2)
obj1=calculator(10,30)
obj1.display()
