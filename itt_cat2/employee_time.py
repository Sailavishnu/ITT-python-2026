starttime=input()
endtime=input()
s_time=int(starttime[10:13])
e_time=int(endtime[10:13])
duration=e_time - s_time
if e_time<s_time:
    print("INVALID")
if duration>5:
    print(duration-1)