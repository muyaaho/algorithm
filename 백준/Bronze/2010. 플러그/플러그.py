import sys
input = sys.stdin.readline

a = 0
n = int(input())
for _ in range(n):
    a += int(input())

print(a-n+1)