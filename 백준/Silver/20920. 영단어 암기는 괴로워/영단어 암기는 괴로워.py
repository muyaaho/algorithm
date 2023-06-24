from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
arr = [x for x in arr if len(x)>=m]

c = Counter(arr)
# print(c)
d = dict()

for x, num in c.items():
    if num in d:
        d[num].append(x)
    else:
        d[num] = [x]
d = sorted(d.items(), reverse=True)
# print(d)

for cnt, arr in d:
    if len(arr) == 1:
        print(*arr)
    else:
        s = sorted(arr, key = lambda x:[-len(x), x])
        print(*s, sep='\n')