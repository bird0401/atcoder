from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

s=sorted(input())
t=sorted(input(),reverse=True)
print(["No","Yes"][s<t])