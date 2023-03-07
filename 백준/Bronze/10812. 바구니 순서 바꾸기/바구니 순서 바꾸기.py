import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(range(1, n+1))

for _ in range(m):
    begin, end, mid = map(int, input().split())
    arr = arr[:begin-1] + arr[mid-1:end] + arr[begin-1:mid-1] + arr[end:]

print(*arr)