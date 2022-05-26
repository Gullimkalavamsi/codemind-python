n=int(input())
s=n*n
a=0
while(s!=0):
    i=s%10
    s=s//10
    a=a+i
if(a==n):
    print('Neon Number')
else:
    print('Not Neon Number')