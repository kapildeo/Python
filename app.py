weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K" :
    converted = int(weight)/0.45
    print(converted)
else:
    converted = int(weight) * 0.45
    print(converted)

print("Done")

print(__name__)