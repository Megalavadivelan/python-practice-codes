class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(person):
    def __init__(self,employee_id):
        self.employee_id=employee_id
    def show_employee(self):
        print("Employee_id:",self.employee_id)
class student(person):
    def __init__(self,roll_no):
        self.roll_no=roll_no
    def show_student(self):
        print("Student's roll_no:",self.roll_no)
class intern(Employee,student):
    def __init__(self,project):
        self.project=project
    def show_intern(self):
        print("project:",self.project)

p1=person("john","12")
p1.show_person()
e1=Employee("1223")
e1.show_employee()
s1=student("23456sfg")
s1.show_student()
i1=intern("to-do-list")
i1.show_intern()
