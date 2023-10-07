import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

m = int(input())
C = list(map(int, sys.stdin.readline().split()))


cnt = 0
for i in reversed(range(n)):
    if cnt<m:
        if A[i] == 0:
            print(B[i], end=' ')
            cnt += 1
    else:
        break

for c in C:
    if cnt < m:
        print(c, end=' ')
        cnt += 1
    else:
        break