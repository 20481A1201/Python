N=10
k=int(input('enter no. of candies'))
if k in range(1,6):
 print('NUMBER OF CANDIES SOLD',k)
 print("NUMBER OF CANDIES AVAILABLE",N-k)
else:
 print('INVALID INPUT')
 print('No. of candies are ',N)
