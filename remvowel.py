str=input("Enter a string")
s=''
for i in str:
 if i in 'aeiouAEIOU':
 pass
 else:
 s=s+i
print("After removing vowels the string is:",s)
