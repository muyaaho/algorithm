import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

y, m = 0, 0

for x in arr:
    y += (x//30 + 1)*10
    m += (x//60 + 1)* 15

if y<m:
    print(f'Y {y}')
elif y == m:
    print(f'Y M {y}')
else:
    print(f'M {m}')