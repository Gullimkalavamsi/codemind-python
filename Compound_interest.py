principle,rate,time=map(int,input().split())
Ci=principle*pow((1+rate/100),time)
print('%.2f'%Ci)