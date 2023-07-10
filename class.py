class invalidmarksrange(Exception):
 def __init__(self,marks):
 self.marks=marks
class Student:
 name=None #class variable 
 def getDetails(self):
 self.marks=[] #instance variable
 try: 
 self.name=input("Enter name of the Student")
 self.marks=[int(i) for i in input('Enter marks in three subjects').split(',')]
 if(len(self.marks)==3):
 s.display()
 s.totalpercent()
 else:
 raise invalidmarksrange('error')
 except(invalidmarksrange):
 print('error')
 def display(self):
 print("Name is:",self.name)
 print('Marks in three subjects',self.marks)
 def totalpercent(self):
 s=0
 for i in self.marks:
 s=s+i
 print('Total marks are:',s)
 print("Total percentage is",(s/300)*100)
s=Student()
s.getDetails()
