n=int(input("enter amount "))
dis=(n*.2 if n>=5000 else (n*.1 if n>=3000 else 0))
print(" bill is " , n-dis)