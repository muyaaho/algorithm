from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
narr = list(map(int, input().split()))

m = int(input())
marr = list(map(int, input().split()))
c = Counter(narr)
for x in marr:
    print(c[x], end=' ')