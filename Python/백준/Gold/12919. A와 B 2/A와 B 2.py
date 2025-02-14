import sys
sys.setrecursionlimit(10**8)

S = input().strip()
T = input().strip()


def AB(string):
    if len(string) == len(S):
        return string == S

    if string[-1] == "A":
        if AB(string[:-1]):
            return True

    if string[0] == "B":
        if AB(string[:0:-1]):
            return True

    return False
    

print(int(AB(T)))