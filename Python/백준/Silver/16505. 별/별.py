import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 0:
        return ['*']

    prev = star(n-1)
    m = 2**(n-1)
    r = []

    for i in range(m):  # 윗부분 (별)
        r.append(prev[i] * 2) # 기존 패턴 2배 확장

    for i in range(m):  # 아랫부분 (별 + 공백)
        r.append(prev[i] + ' ' * m)  # 오른쪽 부분 공백

    return r

N = int(input())
for i in star(N):
    print("".join(i).rstrip())  # 리스트를 한번에 출력하여 속도 최적화

