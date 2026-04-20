t=int(input("enter time t :"))
h_tot=int(input("enter total time :"))
if h_tot<24 or (h_tot&1 ==1 ) or t>=h_tot:
    print("invalid input !")
else:
    d=(h_tot-18*t)//6
    h=t-d
    if d<0 or h<0:
        print("invalid input !")
    else:
        print(f"d: {d} and h :{h}")

'''Read T and H_total.

 is odd, or less than 24, or if 
 is too large. If so, print "INVALID INPUT".
Calculate D using the formula: (H_total - 18 * T) // 6.
Calculate H using: T - D.
Print the result in the format D = 10, H = 5


'''
