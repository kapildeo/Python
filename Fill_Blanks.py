array1 = [1,None,2,3,None,None,5,None]

def solution(nums):

    a=0
    v=[]
    for i in nums:
        if i is not None:
            v.append(i)
            a=i
        else:
            v.append(a)
    return v

print(solution(array1))