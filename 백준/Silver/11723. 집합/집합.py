import sys
input = sys.stdin.readline

n = int(input())
arr = set()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'add':
        arr = arr|{cmd[1]}
    elif cmd[0] == 'remove':
        arr = arr - {cmd[1]}
    elif cmd[0] == 'check':
        if not arr or cmd[1] not in arr:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'toggle':
        if len(arr) == 0 or cmd[1] not in arr:
            arr.add(cmd[1])
        else:
            arr.remove(cmd[1])
    elif cmd[0] == 'all':
        arr = set(map(str,range(1,21)))
    elif cmd[0] == 'empty':
        arr = set()
