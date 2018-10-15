# def exceptions_handling():
#     try:
#         a = 30
#         b = 0
#         c = 20
#
#         d = (a/b)-c
#         print(d)
#     except:
#         print("Zero Division Exception")
#         raise Exception("this is an exception")
#     else:
#         print("Bcos no exception found")
#     finally:
#         print("this will execute always")
#
#
# exceptions_handling()
# print(x)

def exceptions_handling1():
    car = {"make": "BMW", "model": "x3", "Year": 2016}
    try:
        print(car["year"])
    except:
        print("exception here")
    finally:
        print("this will final statement")


exceptions_handling1()