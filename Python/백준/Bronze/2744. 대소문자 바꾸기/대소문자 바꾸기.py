string = input()
ans = ""

for i in string:
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()
        
print(ans)