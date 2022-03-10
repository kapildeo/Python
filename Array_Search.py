from array import *
arr = array('i',[])
x = int(input("what is the length of your array"))

for i in range(x):
    y = int(input("Enter your number"))
    arr.append(y)
print(arr)

z = int(input("which numb you want to search:"))

a = arr.index(z)

print(a)