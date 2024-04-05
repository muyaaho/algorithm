import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [(j, i) for i, j in enumerate(map(int, input().split()), start = 1)]

arr.sort()
q = deque()
q.append(arr[0][1])

for left, node in arr[1:]:
    idx, cnt = 0, 0
    for i in range(len(q)):
        if q[i] > node:
            cnt += 1
            if cnt > left:
                break
        idx += 1
    q.insert(idx, node)
print(*q)