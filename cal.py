n=int(input('Enter weight'))
if(n==0):
 print('Time estimated: 0 Min')
elif n in range(1,2001):
 print('Time estimated: 25 Min')
elif n in range(2001,4001):
 print('Time estimated: 35 Min')
elif n in range(4001,7001):
 print('Time estimated: 45 Min')
elif(n>7000):
 print("Overloaded")
else:
 print('Invalid input')
