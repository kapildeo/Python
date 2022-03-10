y = input("what is your number")
x = int(y)

for i in range(2,x):
    if x % i == 0:
        print("Not Prime")
        break
else:
    Print("Not Prime")
