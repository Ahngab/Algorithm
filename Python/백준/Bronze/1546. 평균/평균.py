N = int(input())
scores = list(map(int, input().split()))
originalMean = sum(scores)/len(scores)

print(originalMean/max(scores)*100)