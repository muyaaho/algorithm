from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

c = Counter(arr)
print(c.most_common(1)[0][0])