import sys
alph = {}
for i in range(97,123):
    alph[chr(i)] = 0

sentence = list("".join([i.strip() for i in sys.stdin.readlines()]))


for i in sentence:
    if i.isalpha():
        alph[i] += 1

max_num = max(alph.values())
for i in alph:
    if alph[i] == max_num:
        print(i,end="")