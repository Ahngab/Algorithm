A, B = input().split()
print(max(int("".join(A[::-1])), int("".join(B[::-1]))))