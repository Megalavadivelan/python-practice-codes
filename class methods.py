class laptop():
    chargertype="C-type"
    def __init__(self):
        self.brand=" "
        self.price=24
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="B-type"
        print("Charger type is changed to b-type")

    @staticmethod
    def info():
        print("This is laptop class")

dell=laptop()
dell.setprice(60000)
dell.getprice()
dell.changechargertype()
dell.info()
