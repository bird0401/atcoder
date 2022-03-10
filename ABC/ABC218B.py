x=list(map(int, input().split()))
ans=""
for e in x:
    ans+=chr(96+e)
print(ans)