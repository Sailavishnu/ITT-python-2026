a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=input("enter operator:")
if c=='+':
   res=a+b
elif c=='-':
   res=a-b
elif c=='*':
   res=a*b
elif c=='/':
   res=a/b
print("the result:",res)