word = input()
result = []
for i in range(97, 123):
    result.append( word.find(chr(i)))
print(*result)