suresh=int(input("enter suresh coin:"))
sundar=int(input("enter sundar coin:"))
raja=int(input("enter raja coin:"))
suresh1=int(input("enter suresh1 coin:"))
if suresh>=sundar:
    sundar+=raja
else:
    suresh+=raja
    
if suresh>=sundar:
    sundar+=suresh1
else:
    suresh+=suresh1
    
if suresh>=sundar:
    print("N")
else:
    print("S")
