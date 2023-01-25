from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    a = input()
    try:
        cmd, num = a.split()
    except ValueError:
        cmd = a.rstrip()

    if cmd == 'push':
        q.append(num)
    elif cmd == 'pop':
        if len(q):
            print( q.pop())
        else:
            print( -1)
    elif cmd == 'size':
        print( len(q))
    elif cmd == 'empty':
        print( 0 if len(q) else  1)
    elif cmd == 'top':
        if len(q):
            print( q[-1])
        else:
            print( -1)
    else:
        print(cmd, '없는 명령어')
    
