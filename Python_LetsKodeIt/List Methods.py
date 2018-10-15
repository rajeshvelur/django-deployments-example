"""
Built in methods to help manipulate LIST
"""

# cars = ["bmw", 'honda', 'volvo']
#
# length = len(cars)
# print(length)
#
# x = cars.index('volvo')
# print(x)
#
# cars.append("benz")
# print(cars)
#
# y = cars.pop()
# print(y)
# print(cars)
# cars.append("benz")
#
#
# print(cars)
# cars.remove('volvo')
#
# print(cars)


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

fib(5)