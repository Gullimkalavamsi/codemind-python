n=int(input())
s=0
a=n
while n>0:
    rem=n%10
    s=s*10+rem
    n=n//10
if s==a:
    print(True)
else:
    print(False)