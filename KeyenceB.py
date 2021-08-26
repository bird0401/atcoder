from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=input()
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[:i]+s[j:]=="keyence":
            print("YES")
            exit()
print("NO")