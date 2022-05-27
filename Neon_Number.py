n=int(input())
s=n*n
r=0
while(s!=0):
    i=s%10
    s=s//10
    r=r+i
if(r==n):
    print('Neon Number')
else:
    print('Not Neon Number')