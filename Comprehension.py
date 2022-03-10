nums = [1,2,3,4,5,6,7,8]

numsq_list = [n*n for n in nums ]
even_list = [n for n in nums if n%2==0]
tups_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(numsq_list)
print(even_list)
print((tups_list))


#Dictionary Comphre

first_name = ('kapil' ,'apurva' ,'manu' ,'maha')
last_name = ('Deo','Srivastava','Dev','Dev')
my_dic = {first_name:last_name for first_name,last_name in zip(first_name,last_name) if first_name=='kapil'}
print(my_dic)


## Set Comprehension

nums = [1,1,1,2,2,2,3,4,5,5,5,5,6,7,8]

sets = {n for n in nums}
print(sets)