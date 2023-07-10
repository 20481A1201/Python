from math import gcd
a,b=int(input("enter first value")),int(input("enter Second value"))
print("GCD is:",gcd(a,b))
print("LCM is:",a*b//gcd(a,b))
