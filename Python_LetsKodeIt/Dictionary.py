"""
dictionary
"""

# cars = {"make": 'bmw', "model":'320i','year':2019}
#
# print(cars)


# x = 0

# while x < 10:
#     print("the value of x:" +str(x))
#     x=x+1
#
#     if x ==6:
#         continue
#     print("this example is for fun")
#     print("*" *20)
#         #break
#
# print("this prints outside of the loop")

#
# x=0
# while x < 10:
#     print("the value of x:" +str(x))
#     x=x+1
#
#     if x ==6:
#         break
#     print("this example is for fun")
#     print("*" *20)
#         #break
# else:
#    print("this prints outside of the loop")


# string = "abcabc"
#
# for i in string:
#     if i=="a":
#         print("A", end=' ')
#     else:
#         print(i)
#
#
# print("*"*20)
# tupleex = (1,2,3)
# print(tupleex)
# for i in tupleex:
#     print(i)
#
# a = "   Hello, World!       "
# print(a[2:5])
# print(a.rstrip())
#
# x=20
# y=10
#
# z = x//y
# print(z)
#
# if x is y:
#     print(x)
# elif x is not y:
#     print(y)
# else:
#     print("anything")
#
# a=20
# b=30
#
# print("A is greater") if a > b else print("A and B are equal") if a == b else print("B is greater")
#
#
# def my_function():
#   print("Hello from a function")
#
# my_function()
#
# def my_function(fname):
#   print(fname + " Refsnes")
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
#
#
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
#
#
# def my_function(x):
#   return 5 * x
#
# my_function(3)
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))



# colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
# for key, value in colours.items():
#     print(key, value)
#
# print("**"*30)
#
# from collections import OrderedDict
#
# colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
# for key, value in colours.items():
#     print(key, value)

#
# from collections import Counter
#
# colours = (
#     ('Yasoob', 'Yellow'),
#     ('Ali', 'Blue'),
#     ('Arham', 'Green'),
#     ('Ali', 'Black'),
#     ('Yasoob', 'Red'),
#     ('Ahmed', 'Silver'),
# )
#
# favs = Counter(name for name, colour in colours)
# print(favs)
#
# from collections import deque
#
# d = deque()
# d.append('1')
# d.append('2')
# d.append('3')
# print(len(d))
# d.clear()
# print(len(d))
#
#
# from collections import namedtuple
#
# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="perry", age=31, type="cat")
#
# print(perry)
# # Output: Animal(name='perry', age=31, type='cat')
#
# print(perry.name)
# # Output: 'perry'
#
# bob = ('Bob', 30, 'male')
# print('Representation:', bob)
#
# jane = ('Jane', 29, 'female')
# print('\nField by index:', jane[1])


# a = list(range(2,8,2,))
# print(a)
#
#
# l = [2,3,4,5]
# for i in range(0,10):
#     print(i)


def sum_num(a,b):
    """
    
    :param a:
    :param b:
    :return:
    """
    return (a+b)

x = sum_num(2,3)
print(x)