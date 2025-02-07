data = list(input())
queue = []
result = []
queue_flag = False

for i in range(len(data)):
    if data[i] == "<":
        for i in list(reversed(queue)):
            result.append(i)

        queue = []
        queue.append("<")
        queue_flag = True

    elif data[i] == ">":
        queue.append(data[i])
        for j in queue:
            result.append(j)
        queue = []
        queue_flag = False
    
    elif data[i] == " " and not queue_flag:
        for j in list(reversed(queue)):
            result.append(j)
        result.append(" ")
        queue = []
    
    else:
        queue.append(data[i])

if len(queue) > 0:
    for i in list(reversed(queue)):
        result.append(i)
print("".join(result))
    
    
        