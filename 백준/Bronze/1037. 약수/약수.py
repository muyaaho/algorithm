import sys 
input = sys.stdin.readline
from math import lcm

cnt = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = lcm(*arr)

print(ans*arr[0] if ans in arr else ans)