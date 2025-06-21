class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name:",self.name)
        print("Regno:",self.regno)

t1=teacher("latha","234")
t2=teacher("priya","345")
t1.display()
t2.display()
