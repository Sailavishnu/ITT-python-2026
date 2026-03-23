mail=input("enter mail:")
at_index = mail.find("@")
dot_index = mail.rfind(".")

if at_index > 0 and dot_index > (at_index + 1) and not mail.endswith("."):
    flag = True
else:
    flag = False

print("Valid" if flag else "Invalid")

'''
'find("@")' gets the position of the @ symbol.
'rfind(".")' gets the position of the LAST dot (the one in .com).
'@' must not be the very first character (at_index > 0).
There must be at least one character between '@' and '.' (dot_index > at_index + 1).
The email cannot end with a dot (not mail.endswith(".")).
'''