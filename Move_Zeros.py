array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def movezero(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

print(movezero(array1))
print(movezero(array2))