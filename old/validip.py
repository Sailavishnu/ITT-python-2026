ip=input("enter the ip:")
a=ip.split('.')
flag=False
if len(a)==4:
    flag=True
    for i in a:
        if i.isdigit():
            if not 0<= int(i) <=255:
                flag=False
                break
        else:
            flag=False
            break
        
print(flag)

'''

Split the text by dots ,should have exactly 4 parts.
Fo each part, check if it's only numbers .
If it's a number, check if it's in the valid range (0 to 255).
'''
