'''
set - Pypy3로 겨우 됨
dp처럼 인덱스로 값을 접근하면 훨씬 빠르게 가능

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*21

# print(0 == False)
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'all':
        arr = [1] * 21
    elif cmd[0] == 'empty':
        arr = [0] * 21
    else:
        x = int(cmd[1])
        if cmd[0] == 'add':
            arr[x] = 1
        elif cmd[0] == 'remove':
            arr[x] = 0
        elif cmd[0] == 'check':
            print(1 if arr[x] else 0)
        elif cmd[0] == 'toggle':
            arr[x] = 0 if arr[x] else 1
