import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1

T = int(input())
time = {}
cnt = 0
for _ in range(T):
    t, dir = map(str, input().split())
    time[int(t)] = dir

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nd, hx, hy = 0, 0, 0
body = deque()
body.append((hx, hy))

while True:
    cnt += 1
    hx += dx[nd]
    hy += dy[nd]
    if hx < 0 or hx >= N or hy < 0  or hy >= N or (hx, hy) in body:
        break
    body.append((hx, hy))

    if board[hx][hy] == 0:
        body.popleft()
    else:
        board[hx][hy] = 0

    if cnt in time:
        if time[cnt] == "L":
            nd = (nd - 1) % 4
        else:
            nd = (nd + 1) % 4

print(cnt)
