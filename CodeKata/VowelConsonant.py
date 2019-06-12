char=input()
v=['a','e','i','o','u','A','E','I','O','U']
if(char.isalpha()):
  if(char in v):
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
