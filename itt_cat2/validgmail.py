mail=input("enter mail:")
at_index = mail.find("@")
dot_index = mail.rfind(".")
space_index=mail.find(" ")

if at_index > 0 and dot_index > (at_index + 1) and mail!=" " and space_index!=0 and mail.count("@") ==1:
    flag = True
else:
    flag = False

print("Valid" if flag else "Invalid")