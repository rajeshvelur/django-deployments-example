"""
file I/O
r - Read
w - Write
r+ -Read and Write
a - Append
"""

myList = [1,2,3]
myFile = open("mytextfile.txt", "w")

for i in myList:
    myFile.write(str(i) + "\n")

myFile.close()