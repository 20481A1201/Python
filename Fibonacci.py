def fib(k):
 a,b,s=0,1,0
 while(k>0):
print(a,end=‟ „)
 if(a%2==0):
 s=s+a
 c=a+b
 a=b
 b=c
 k=k-1
 print("\nEven valued fib. sum is",s)
n=int(input('Enter an Integer'))
fib(n)
