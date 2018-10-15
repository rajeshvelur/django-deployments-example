"""
Modules demo
"""

# import math
from math import sqrt
# import ModulesExternal
# from ModulesExternal import car
from ModulesExternal.car import car_info

class ModulesDemo():

    def builtinmeth(self):

        # print(math.sqrt(100))
        print(sqrt(100))

    def cardesc(self, make = "AUDI", model = "AUDI-S3"):
        make = "BMW"
        model = "x5"
        car_info(make, model)


m = ModulesDemo()
m.builtinmeth()

m.cardesc("toyota", "camry")


