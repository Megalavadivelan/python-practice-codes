class animal():
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class bird(animal):
    def sound(self):
        print("Birds sing")
A1=bird()
A1.sound()
