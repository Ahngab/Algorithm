N = int(input())
words = []
queue = []
for i in range(N):
    word = input()
    if word not in queue:
        words.append([word, len(word)])
        queue.append(word)

words = sorted(words, key=lambda x: (x[1], x[0]))
for i in words:
    print(i[0])