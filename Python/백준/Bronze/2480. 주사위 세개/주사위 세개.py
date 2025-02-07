data = list(map(int, input().split()))
dic = {}

#몇 개 인지 나타내는 dic 만들기
for i in data:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
#print(dic)

if len(dic) == 1:
    print(max(dic.keys()) * 1000 + 10000)
elif len(dic) == 2:
    print({k:v for v,k in dic.items()}.get(max(dic.values())) * 100 + 1000)
else:
    print(max(dic.keys())*100)