def quiz(data):
    data = list(data)
    temp = 0
    score = 0

    for i in data:
        if i == "O":
            temp += 1
        else:
            temp = 0
        score += temp

    return score

N = int(input())

for i in range(N):
    data = input()
    print(quiz(data))