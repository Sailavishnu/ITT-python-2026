balance=500
n=int(input("enter amount: "))
print("you can withdraw" if n>0 and n%100==0 and n<balance else " you can't withdraw ")