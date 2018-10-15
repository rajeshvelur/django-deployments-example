class fruit(object):

    def __init__(self):
        print("this is a fruit class initialization")
    def nutrition(self):
        print("this is a Fruit-Nutrition method")
    def fruit_shape(self):
        print("this is a Fruit Shape method")

class apple(fruit):

    def __init__(self):
        # super().__init__()
        fruit.__init__()
        print("this is apple class initialization")
    def nutrition(self):
        print("this is Apple-Nutrition method")
    def color(self):
        print("this is Apple-Color method")

f = fruit()
f.fruit_shape()
f.nutrition()
print("*"*50)
a = apple()
a.nutrition()
a.color()
a.fruit_shape()