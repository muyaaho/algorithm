from itertools import combinations
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

c = combinations(arr, m)
for x in list(c):
    print(*x)