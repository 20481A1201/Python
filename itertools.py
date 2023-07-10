import itertools
print("count() function")
for i in itertools.count(10,10):
if(i==100):
break
else:
print(i,end=' ')
print("cycle() function")
c=1
for i in itertools.cycle("SRGEC"):
if(c>=5):
break;
else:
c=c+1
print(i,end=' ')
print("repeat() function")
print(list(itertools.repeat(20,5)))
print("product() function")
print(list(itertools.product('gec','IT','CSE')))
a=[3,4]
b=[10,20]
print(list(itertools.product(a,b)))
print("permutations() function")
print(list(itertools.permutations("GEC")))
print("Combinations() function")
print(list(itertools.combinations('gec',2)))
print("compress() function")
print(list(itertools.compress('srgec',[1,0,1,1,0])))
print("chain() function")
print(list(itertools.chain([2,3,4],[10,29,30],[34])))
