n=int(input("enter your mark :"))
if n>=90:
   grade='A'
elif n>=75 and n<90:
   grade='B'
elif n>=60 and n<70:
   grade='C'
else:
   grade='D'
print("your grade is :",grade)
