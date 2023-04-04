import sys
input = sys.stdin.readline

arr = set()
for _ in range(int(input())):
    name, cmd = input().split()
    if cmd == 'enter':
        arr.add(name)
    else:
        arr.remove(name)

print(*sorted(arr, reverse=True),sep='\n')