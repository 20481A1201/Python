import math
s=0
def strlength(s):
 if s=='':
 return 0
 else:
 return 1+strlength(s[1:])
def palindrome(k):
 global s,n
 a=k
 if(a>0):
 s=s*10+a%10
 a//=10
 return palindrome(a)
 else:
 if(n==s):
 return True
 else:
 return False
str=input("Enter a string")
print("Length of the given string is:",strlength(str))
n=int(input("Enter a number"))
if(palindrome(n)):
 print(abs(n),'is a palindrome')
else:
 print(abs(n),'is not a palindrome')
