n = int(input())

if (n **0.5) % 1 == 0:
    print(1)

else:
    min_ = 4
    i = 1
    arr = []
    while i**2 <= n:
        arr.append(i**2)
        i += 1
    arr = arr[::-1]

    flag = False

    min_  = 4
    for i in range(len(arr)):
        if ((n - arr[i])**0.5) % 1 == 0:
            min_ = 2
            break

        else:
            for j in range(len(arr)):
                tmp = n - arr[i] - arr[j]
                if tmp >= 0 and (tmp**0.5)%1 == 0:
                    min_ = 3

                    
        
    print(min_)