import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = sys.stdin.readline
N = int(input())
Q = deque()
graph = {}
for _ in range(N):
    Root, Left, Right = input().split()
    graph[Root] = [Left, Right]

def front(root):
    if root == '.':
        return 
    else:
        left, right = graph[root][0], graph[root][1]
        print(root, end="")
        front(left)
        front(right)

def mid(root):
    if root == '.':
        return 
    else:
        left, right = graph[root][0], graph[root][1]
        mid(left)
        print(root, end = "")
        mid(right)

def back(root):
    if root == '.':
        return 
    else:
        left, right = graph[root][0], graph[root][1]
        back(left)
        back(right)
        print(root, end = "")

front("A")
print()
mid("A")
print()
back("A")
