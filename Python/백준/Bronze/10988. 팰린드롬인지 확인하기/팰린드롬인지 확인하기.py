word = list(input())
flag = True

for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        flag = False
        break
print(1) if flag else print(0)