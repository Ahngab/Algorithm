import sys

input = sys.stdin.readline
words = {}
M, N = map(int, input().split())

for _ in range(M):
    word = input().strip()

    if len(word) < N:
        continue
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sortedList = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in sortedList:
    print(i[0])