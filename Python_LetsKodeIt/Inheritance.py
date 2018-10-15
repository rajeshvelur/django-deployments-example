
class Car(object):

    def __init__(self):
        print("this is car class")
    def start(self):
        print("this is Car - Start method")
    def stop(self):
        print("this is the car - stop")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("this is the BMW class")

    def start(self):
        super(Car, self).start()
        super().stop()
        print("this is BMW start")
    def unique_feature(self):
        print("this is a unique feature")

# c = Car()
# c.stop()
# c.start()


b = BMW()
b.start()
# b.unique_feature()