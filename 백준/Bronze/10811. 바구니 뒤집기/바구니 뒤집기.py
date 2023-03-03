import sys
input =sys.stdin.readline

n, m = map(int, input().split())
arr = list(range(n+1))
for x in range(m):
    i, j = map(int, input().split())
    arr = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
print(*arr[1:])