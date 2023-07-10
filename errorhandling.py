import math
try:
 d={1:'IT',2:'CSE',3:'EEE'}
 a=int(input('Enter a key value'))
 print(d[a])
 b=int(input("Enter a number to find factorial"))
 print(math.factorial(b))
except(KeyError,ValueError):
 print('Error')
else:
 print('Executed Successfully')
