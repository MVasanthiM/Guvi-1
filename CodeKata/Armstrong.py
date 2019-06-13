def arm():
  s=0
  t=num
  while(t>0):
    c=t%10
    s+=c**3
    t//=10
  if(num==s):
    print('yes')
  else:
    print('no')
num=int(input())
arm()
