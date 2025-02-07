words = []
result = ""

for _ in range(5):
    temp = input()
    temp += " "*(15- len(temp))
    words.append(temp)

for i in range(15):
    for j in range(5):
        if words[j][i] != " ":
            result += words[j][i]
print(result)