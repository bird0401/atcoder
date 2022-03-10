from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=list(input())
for i in range(ord('a'),ord('z')+1):
    if chr(i) not in s:
        print(chr(i))
        exit()
print("None")
