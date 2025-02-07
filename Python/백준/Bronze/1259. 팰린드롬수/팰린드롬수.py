while True:
    check = input()
    if check != "0":
        if len(check) %2 == 0:
            half_1 = check[:len(check)//2]
            half_2 = ''.join(reversed(check[len(check)//2:]))
            if half_1 == half_2:
                print("yes")
            else:
                print("no")
        else:
            half_1 = check[:len(check)//2]
            half_2 = ''.join(reversed(check[len(check)//2+1:]))
            if half_1 == half_2:
                print("yes")
            else:
                print("no")
    else:
        break