import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

warr = [0, w]
harr = [0, h]
for _ in range(n):
    c, a = map(int, input().split())
    if c == 0:
        harr.append(a)
        continue
    warr.append(a)

harr.sort()
warr.sort()

answer = 0
for i in range(len(warr)-1):
    for j in range(len(harr) -1):
        x = warr[i+1] - warr[i]
        y = harr[j+1] - harr[j]
        answer = max(answer, x * y)

print(answer)