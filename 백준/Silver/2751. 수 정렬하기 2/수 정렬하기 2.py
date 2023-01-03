import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
for x in sorted(l):
    print(x)