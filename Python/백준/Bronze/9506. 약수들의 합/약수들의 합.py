while True:
    n = int(input())
    factor = []
    sum_ = 0

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            factor.append(i)
            sum_ += i

    if n == sum_:
        print(n, "= ", end="")
        print(*factor, sep=" + ")
    
    else:
        print(n,"is NOT perfect.")