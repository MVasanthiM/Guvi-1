sr,er=map(int,input().split())
for num in range(sr+1,er):
  sum=0
  temp=num
  while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
  if(num==sum):
    print(num,end=' ')
