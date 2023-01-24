import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
# 평균
print(round(sum(arr)/n))

# 중앙값
print(arr[(n-1)//2])

# 최빈값
c = Counter(arr).most_common(2)
print(c[1][0] if len(arr)>1 and c[0][1] == c[1][1] else c[0][0])

# 범위
print(arr[-1] - arr[0])