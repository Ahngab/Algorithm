T = int(input())

for _ in range(T):
    N = int(input())
    numQuarter = N // 25
    N = N % 25
    numDime = N // 10
    N = N % 10
    numNickel = N // 5
    numPenny = N % 5
    print(numQuarter, numDime, numNickel, numPenny)