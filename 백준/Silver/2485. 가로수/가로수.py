import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
arr = [int(input()) for _ in range(n)]

b = []
bf = arr[-1]
for x in arr[:-1][::-1]:
    b.append(bf-x)
    bf = x

g = gcd(*b)
answer = sum([x//g-1 for x in b])

print(answer)