t=int(input("enter time t:"))
m_tot=int(input("enter total minute m total:"))
numarator=(3*m_tot -10*t)

if m_tot<60 or (m_tot%10 !=0) or t>=m_tot or (numarator %170 !=0):
    print("invalid")
else:
    h=numarator//170
    m=t-h
    if h<0 or m<0:
        print("invalid")
    else:
        print(f"H = {h} , M = {m}")


'''
Read T and M_total.
Use an if statement to check if 
M_total is less than 60, or if 
M_total is not a multiple of 10, or if 
T is too large (T >= M_total). If so, print "INVALID INPUT".

Calculate H using the formula: (3 * M_total - 10 * T) // 170.
Calculate M using: T - H.

Print the result in the format H = 40, M = 30
'''