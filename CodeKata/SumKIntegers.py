a,b=map(int,input().split())
l=[]
sum=0
l=map(int,input().split())
l1=list(l)
if(len(l1)==a):
  for i in range (len(l1)):
    if(i<b):
      sum=sum+l1[i]
  print(sum)
