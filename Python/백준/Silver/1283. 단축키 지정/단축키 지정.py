def find_first(word):
    global alpha

    words = word.split()
    for i in range(len(words)):
        if words[i][0].lower() not in alpha:
            alpha.append(words[i][0].lower())
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            break

    return " ".join(words).rstrip()

def second_find(word):
    global alpha
    flag = False

    word = word.split()
    for i in range(len(word)):
        for j in range(len(word[i])):
            if word[i][j].lower() not in alpha and word[i][j].isalpha():
                alpha.append(word[i][j].lower())
                word[i] = str(word[i][:j]) + "[" + str(word[i][j]) + "]" + str(word[i][j+1:])
                flag = True
                break
        if flag:
            break


    return " ".join(word).rstrip()


if __name__ == "__main__":
    alpha = []
    N = int(input())
    data = [input() for _ in range(N)]
    result =[]
    for i in data:
        first = find_first(i)
        if "[" not in first:
            second = second_find(i)
            if "[" not in second:
                result.append(i)
            else:
                result.append(second)
        else:
            result.append(first)

    for i in result:
        print(i)

