H, M = map(int, input().split())
timeTake = int(input())

minutes = 60*H + M + timeTake

if minutes >= 1440:
    minutes -= 1440

H = minutes//60
M = minutes - H*60

print(H, M)