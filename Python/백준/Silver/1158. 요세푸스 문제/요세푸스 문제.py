N, K = map(int, input().split())

people = [i for i in range(1, N + 1)]
order = []
num = 0

for j in range(N):
    num += K - 1
    if num >= len(people):
        num = num % len(people)
    order.append(str(people.pop(num)))

print("<", ", ".join(order), ">",sep='')
