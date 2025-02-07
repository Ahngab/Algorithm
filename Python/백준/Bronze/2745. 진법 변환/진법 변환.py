N, B = input().split()
B = int(B)
target = 0

for i in range(len(N)):
    letter = ord(N[i])
    if letter >= 65:
        letter -= 55
    elif letter <= 57:
        letter -= 48
    target += B**(len(N) - i-1) * letter
print(target)
