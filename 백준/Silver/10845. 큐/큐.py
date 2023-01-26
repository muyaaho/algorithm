from collections import deque
import sys
input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    a = input().rstrip()
    try:
        cmd, num = a.split(' ')
        num = int(num)
    except:
        cmd = a
    
    if cmd == 'push':
        q.append(num)
    elif cmd =='pop':
        if len(q)>0:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(1 if len(q) == 0 else 0)
    elif cmd == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(q)>0:
            print(q[-1])
        else:
            print(-1)
