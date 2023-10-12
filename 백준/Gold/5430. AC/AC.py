import sys
input = sys.stdin.readline
from collections import deque

def list_print(arr, is_reverse):
    if not arr:
        print('[]')
    else:
        if is_reverse:
            arr.reverse()
        print('[' + ','.join(arr)+']')

for _ in range(int(input())):
    cmds = input()
    n = int(input())
    arr = input().rstrip().strip('[]').split(',')
    if n == 0:
        arr = []
    
    is_error = False
    is_reverse = False
    q = deque(arr)
    for cmd in cmds:
        if cmd == 'R':
            is_reverse = not is_reverse
        elif cmd == 'D':
            if not q:
                print('error')
                is_error = True
                break
            else:
                if is_reverse:
                    q.pop()
                else:
                    q.popleft()

    if not is_error:
        list_print(q, is_reverse)  