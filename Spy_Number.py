n=int(input())
s=0
m=1
while(n>0):
    i=n%10
    n//=10
    s=s+i
    m=m*i
if(s==m):
    print('Spy Number')
else:
    print('Not Spy Number')