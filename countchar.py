str=input('Enter a string')
d={}
for i in str:
 d[i]=str.count(i)
for x,y in d.items():
 print(x,'->',y)
