class dad():
    def phone(self):
        print("Dad's phone")
class mom(dad):
    def lunch(self):
        print("Mom prepared lunch for ram")
class son(dad,mom):
    def laptop(self):
        print("Son's laptop")
ram=son()
ram.laptop()
ram.phone()
ram.lunch()
viji=mom()
viji.phone()
