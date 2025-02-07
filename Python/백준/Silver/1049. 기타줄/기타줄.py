N, M = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(M)]
min_package = min(data, key = lambda x: x[0])[0]
min_one = min(data, key = lambda x: x[1])[1]
print(min([(N//6+1)*min_package, (N//6)*min_package+(N%6)*min_one, min_one*N]))