N = int(input("no of marks:"))
print("enter your marks seperated by space:" ,end="")
marks = list(map(int, input().split()))


unique_marks = sorted(list(set(marks)))

frequency_dict = {mark: marks.count(mark) for mark in unique_marks}

if len(unique_marks) < 2:
    second_highest = "NO SECOND HIGHEST"
else:
    second_highest = unique_marks[-2]

print("unique marks :",unique_marks)
print("frequency of each marks: ",frequency_dict)
print("second highest marks : ",second_highest)