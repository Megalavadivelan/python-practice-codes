class goa:
    name=""
    drink=""
    def party(self):
        print("Lets party....")
    def Beach(self):
        print("Lets Enjoy")
Ramesh=goa()
suresh=goa()

Ramesh.name="Ramesh"
suresh.name="suresh"

Ramesh.drink="Yes"
suresh.drink="No"

print("Name:",Ramesh.name)
print("Drink:",Ramesh.drink)

print("Name:",suresh.name)
print("Drink:",suresh.drink)

Ramesh.party()
suresh.Beach()
