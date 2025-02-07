#while True 보통 쓰면 time exceed 뜨니깐 while문에 조건 달아야함.
#이분탐색 문제인듯
import sys

N, need = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

max_height = max(trees)
min_height = 0

while min_height <= max_height:
    num = (max_height + min_height) // 2
    cut = 0
    for i in trees:
        if i > num:
            cut += i - num
    if cut < need:
        max_height = num - 1
    elif cut >= need:
        min_height = num + 1
print(max_height)