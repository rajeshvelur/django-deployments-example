"""
object oriented programming
"""
#****************************
a = "this is my string"
a.lower()
a.upper()

print(type(a))
print("*"*30)
#****************************

class Car(object):

    no_of_wheels = 4
    def __init__(self, make, model="x5"):
        self.make = make
        self.model = model

    def info1(self):
        print("Make of my car is:" + self.make)
        print("Model of my car is : " + self.model)

class BMW():
    def __init__(self):
        print("this is BMW class method")
    def stop(self):
        print("this will stop only BMW")

c= Car("bmw")
print(c.make)
c.info1()
c1= Car('benz', "c350")
print(c1.make)
c1.info1()

