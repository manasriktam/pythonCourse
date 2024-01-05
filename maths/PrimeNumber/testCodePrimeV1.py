t = int(input())
while(t != 0):
    n = int(input())
    flag = True
    if(n<2):
        flag = False
    for i in range(2, n):
        if(n%i==0):
            flag=False
            break
    if(flag):
        print(("{} is a prime number.".format(n)))
    else:
        print("{} is not a prime number.".format(n))
    t = t - 1