amount = int(input("Enter amount: "))

n500 = amount // 500
rem = amount % 500

n200 = rem // 200
rem %= 200

n100 = rem // 100
rem %= 100

if rem==0:
    print("500: ",n500,"\n200: ",n200, "\n100: ",n100)
else:
    print("invalid input")