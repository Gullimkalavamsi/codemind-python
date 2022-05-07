n=int(input())
r=0
a=n
while n>0:
    rem=n%10
    r=r*10+rem
    n=n//10
if r==a:
    print(True)
else:
    print(False)