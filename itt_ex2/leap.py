n=int(input("enter a number :"))
print("leap year " if n%4==0 or (n%400==0 and n%100!=0) else "not a leap year")