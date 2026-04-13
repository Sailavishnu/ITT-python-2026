n=int(input("enter your salary :"))
if n<=250000:
   tax=0
elif n>250000 and n<=500000:
   tax=.05
elif n>500000 and n<=1000000:
   tax=.1
else:
   tax=1.5
salary=n*tax
print("your tax amount is :",salary)
print("your total salary is :",n-salary)