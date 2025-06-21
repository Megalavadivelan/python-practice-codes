class student:
    def __init__(self):
        self.name=""
        self.reg_no=""
    def display(self):
        print("name:",self.name)
        print("reg_no:",self.reg_no)
s1=student()
s2=student()

s1.name="megala"
s2.name="santhiya"

s1.reg_no="49"
s2.reg_no="48"

print(s1.name)
print(s1.reg_no)
s1.display()
s2.display()
