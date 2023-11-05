from collections import Counter

n = int(input())
arr = sorted([input() for _ in range(n)])
print(Counter(arr).most_common()[0][0])