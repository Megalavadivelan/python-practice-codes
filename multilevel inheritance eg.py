class grandfather():
    def money(self):
        print("Grandfather's money")
class dad(grandfather):
    def phone(self):
        print("Dad's phone")
class son(dad):
    def videogame(self):
        print("son's videogame")
s1=son()
s1.videogame()
s1.phone()
s1.money()
d1=dad()
s1.money()
d1.phone()
