num=int(input())
if(num==1):
  print('no')
elif(num==2):
  print('yes')
else:
  for i in range(2,num):
    if(num%i)==0 :
      print('no')
      break
  else:
    print('yes')
