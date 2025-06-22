class dad():
    def phone(self):
        print("Dad's phone")
    def money(self):
        print("Dad's moeny")
class son(dad):
    pass
class daughter(dad):
    pass
class mom(dad):
    pass
son=son()
son.phone()
son.money()
daughter=daughter()
daughter.money()
mom=mom()
mom.money()
mom.phone()
