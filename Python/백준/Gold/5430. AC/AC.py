from collections import deque

def func(string, arr):
    rFlag = False

    for i in range(len(string)):
        if string[i] == "R":
            rFlag = not rFlag

        else:
            if rFlag:
                if arr:
                    arr.pop()
                else:
                    return "error"

            else:
                if arr:
                    arr.pop(0)
                else:
                    return "error"

    if rFlag:
        return "[" + ",".join(list(map(str, arr[::-1]))) + "]"
    else:
        return "[" + ",".join(list(map(str, arr))) + "]"



T = int(input())

for _ in range(T):
    function = input().strip()
    n = int(input())
    tmp = input().strip()
    


    if tmp == "[]":
        print("error" if "D" in function else "[]")
    
    else:
        tmp = tmp.rstrip(']').lstrip("[")
        num = list(map(int, tmp.split(sep=",")))
        print(func(function, num))
