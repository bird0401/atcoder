from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import floor,ceil

a,b,w=map(float,input().split())
w*=1000
da,db=int(floor(w/a)),int(ceil(w/b))
if db>da: print("UNSATISFIABLE")
else: print("{} {}".format(db,da))