data = list(map(int, input().split()))

asc = sorted(data)
desc = sorted(data, reverse = True)

if data == asc:
    print("ascending")
elif data == desc:
    print("descending")
else:
    print("mixed")