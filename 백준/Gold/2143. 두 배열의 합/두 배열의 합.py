from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
aarr = list(map(int, input().split()))
m = int(input())
barr = list(map(int, input().split()))

asum, bsum = [],[]

for i in range(n):
    k = aarr[i]
    asum.append(k)
    for j in range(i+1, n):
        k += aarr[j]
        asum.append(k)

for i in range(m):
    k = barr[i]
    bsum.append(k)
    for j in range(i+1, m):
        k += barr[j]
        bsum.append(k)

asum.sort()
bsum.sort()

answer = 0
for i in range(len(asum)):
    l = bisect_left(bsum, t - asum[i])
    r = bisect_right(bsum, t - asum[i])
    answer += r-l
print(answer)