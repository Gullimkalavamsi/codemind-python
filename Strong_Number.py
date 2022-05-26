n=int(input())
s=0
temp=n
while(n):
    j=1
    fact=1
    i=n%10
    while(j<=i):
        fact=fact*j
        j=j+1
    s=s+fact
    n=n//10
if(s==temp):
    print('The number',temp,'is a strong number')
else:
    print('The number',temp,'is not a strong number')