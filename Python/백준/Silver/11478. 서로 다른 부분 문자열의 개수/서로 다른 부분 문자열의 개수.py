import sys

string = sys.stdin.readline().strip()
dict = set()

for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        target = string[i:j]
        if target not in dict:
            dict.add(target)

print(len(dict))