import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
oper = {0:"+", 1: "-", 2:"*", 3:"/"}
index = 0

result = []
# def check(x, y):
#     return (-1)* abs(x)//y
        

def operation(temp_result, index, op):
    if index == n-1:
        result.append(temp_result)
        return 
    
    else:
        for i in range(4):
            if op[i]  == 0:
                continue
            else:   
                tmp = int(eval(str(temp_result) + oper[i] + str(arr[index+1])))
                op[i] -= 1
                operation(tmp, index+1, op)
                op[i] += 1


operation(arr[0], 0, op)
print(max(result))
print(min(result))

