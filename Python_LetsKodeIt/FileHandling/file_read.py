"""
file read
"""

my_file = open("mytextfile.txt", 'r')

print(str(my_file.read()))

print("*"*30)

my_file1 = open("mytextfile.txt", 'r')
print(my_file1.readline())
print(my_file1.readline())
print(my_file1.readline())

my_file.close()