s=0
def rev(n):
 global s
 if(n>0):
 s=s*10+n%10
 n//=10
 rev(n) #recursive call
 return s
x=int(input('Enter an Integer'))
print("Reverse is:%d"%(rev(x)))
