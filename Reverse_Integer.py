n=int(input())
rev=0
if n>0:
    while n!=0:
        rev=rev*10+n%10
        n=n//10
    print(rev)
else:
    n*=-1
    while n!=0:
        rev=rev*10+n%10
        n=n//10
    print('-'+str(rev))