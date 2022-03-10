from collections import deque
n=int(input())
q=deque(())
for _ in range(n):
    c=input().split()
    if c[0]=="deleteFirst":q.popleft()
    elif c[0]=="deleteLast":q.pop()
    elif c[0]=="insert":q.appendleft(c[1])
    elif c[0]=="delete" and c[1] in q:q.remove(c[1])
    # print(q)
print(*q)

