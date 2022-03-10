array1 = [1,2,3,4]
array2 = [1,2,2,2,3]
def solution(nums):

    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        else:
            hashset.add(i)
    return  False

print(solution(array1))
print(solution(array2))