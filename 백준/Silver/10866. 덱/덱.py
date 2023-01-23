from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
commands = []
q = deque()
for x in range(n):
    line = input().rstrip()
    try:
        cmd, num = line.split(' ')
        num = int(num)
    except:
        cmd = line
    
    if cmd == 'push_back':
        q.append(num)
    elif cmd == 'push_front':
        q.appendleft(num)
    elif cmd == 'pop_front':
        try:
            a = q.popleft()
            print(a)
        except:
            print(-1)
    elif cmd == 'pop_back':
        try:
            a = q.pop()
            print(a)
        except:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif cmd == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
