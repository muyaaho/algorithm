from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

print(round(sum(arr)/n))    # 산술
print(arr[(n-1)//2])        # 중앙값

c = Counter(arr).most_common()  # 최빈값
if len(arr)>1 and c[0][1] == c[1][1]:
    print(c[1][0])
else:
    print(c[0][0])

print(arr[-1]- arr[0])      # 범위