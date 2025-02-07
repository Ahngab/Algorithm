alph = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input()
time = 0

for i in range(len(word)):
    for j in range(len(alph)):
        if word[i] in alph[j]:
            time += (j + 3)

print(time)