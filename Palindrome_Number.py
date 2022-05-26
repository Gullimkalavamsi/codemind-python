x=int(input())
for i in range(x):
    n=int(input())
    r=0
    temp=n
    while(n!=0):
        i=n%10
        r=r*10+i
        n=n//10
    if(temp==r):
        print('True')
    else:
        print('False')