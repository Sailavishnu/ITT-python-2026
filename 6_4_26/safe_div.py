a, b = map(int, input().split())

try:
    if b==0:
        raise ZeroDivisionError
    elif type(b)!=int:
        raise 
    else:
