class student():
    school_name="ABC high School"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("Name:",self.name)
        print("Roll_number:",self.roll_no)
        print("School:",self.school_name)
john=student("JOHN","123")
john.display()

karthik=student("KARTHIK","234")
karthik.display()
