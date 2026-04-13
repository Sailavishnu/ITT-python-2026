a=int(input("enter  number 1:"))
b=int(input("enter  number 2:"))
c=int(input("enter  number 3:"))
second_largest = ((b if b > c else c) if (a >= b and a >= c) else
    (a if a > c else c) if (b >= a and b >= c) else
    (a if a > b else b))
print(second_largest)
