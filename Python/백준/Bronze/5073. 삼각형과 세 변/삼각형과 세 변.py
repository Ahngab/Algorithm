while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    else:
        if max(a, b, c) >= (a + b + c - max(a, b, c)):
            print("Invalid")
        else:
            if a == b and b == c and c == a:
                print("Equilateral")

            elif a == b or b == c or c == a:
                print("Isosceles")
            
            else:
                print("Scalene")