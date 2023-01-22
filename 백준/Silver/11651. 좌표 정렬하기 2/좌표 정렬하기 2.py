import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda x: (x[1], x[0]))
for x in arr:
    print(*x)