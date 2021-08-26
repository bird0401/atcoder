from math import radians,degrees,cos,sin,sqrt,atan
t=int(input())
l,x,y=map(int,input().split())
q=int(input())
for i in range(q):
    e=float(input())
    deg=radians(-90-e/t*360)
    ey,el=l/2.0*cos(deg),l/2.0*sin(deg)+l/2.0
    print(degrees(atan(el/sqrt((ey-y)**2+x**2))))