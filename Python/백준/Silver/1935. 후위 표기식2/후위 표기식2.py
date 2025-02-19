from collections import deque

def calc(x, y, op):
    if op == "+": return x + y
    elif op == "-": return x - y
    elif op == "*": return x * y
    else: return x / y

N = int(input())
string = input().strip()
dict = {}

for i in range(N):
    dict[chr(i + 65)] = int(input())


cal = set(["+", "-", "*", "/"])
queue = deque()

for i in string:
    if i not in cal:
        queue.append(i)
    else:
        num2 = queue.pop()
        if num2.isalpha():
            num2 = dict[num2]
        num1 = queue.pop()
        if num1.isalpha():
            num1 = dict[num1]
        queue.append(str(calc(float(num1), float(num2), i)))

print("%.2f"%float(queue[0]))
    