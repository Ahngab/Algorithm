import sys

N, M = map(int, sys.stdin.readline().strip().split())

A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))

print(len((A-B) | (B-A)))