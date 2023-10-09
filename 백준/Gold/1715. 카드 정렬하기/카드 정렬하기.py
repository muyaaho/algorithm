from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    heappush(arr, int(input()))

answer = 0
while len(arr) > 1:
    a_b = heappop(arr)+heappop(arr)
    answer += a_b
    heappush(arr, a_b)

print(answer)