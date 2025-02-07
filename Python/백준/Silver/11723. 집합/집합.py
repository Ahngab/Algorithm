import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    if len(command) == 1:
        if command[0] == "all":
            S = set([i for i in range(1,21)])

        elif command[0] == "empty":
            S = set()
    else:
        x = int(command[1])
        if command[0] == "add":
            if x not in S:
                S.add(x)

        elif command[0] == "remove":
            if x in S:
                S.discard(x)

        elif command[0] == "check":
            print(1) if x in S else print(0)

        elif command[0] == "toggle":
            S.add(x) if x not in S else S.discard(x)