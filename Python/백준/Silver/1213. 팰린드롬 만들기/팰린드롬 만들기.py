dict = {}
name = input()

for i in name:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

flag = False
No = False
for i in dict.keys():
    if flag and dict[i] % 2 == 1:
        No = 1
    if dict[i] % 2 == 1:
        flag = True
        odd = i

if No:
    print("I'm Sorry Hansoo")

else:
    if len(name) % 2 == 1:
        alph = sorted(list(name))
        alph.remove(odd)
        half_name = alph[::2]
        print("".join(half_name + [odd] + half_name[::-1]))
    else:
        alph = sorted(list(name))
        half_name = alph[::2]
        print("".join(half_name + half_name[::-1]))