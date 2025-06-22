class phone():
    chargertype="c-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)
samsung=phone("Samsung","10000")
samsung.display()

vivo=phone("vivo","20000")
vivo.display()
