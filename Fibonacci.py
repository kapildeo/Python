nterms = int(input("how many term ?"))

#first two terms
n1,n2 = 0,1
count = 0

if nterms<=0:
    print('please enter a +ve number')
elif nterms==1:
    print('Fibonaci series for ', nterms ,":")
    print(n1)
else:
    print("Fib seq is ")
    while count < nterms:
        print(n1)
        nth=n1+n2
        n1= n2
        n2=nth
        count+=1
