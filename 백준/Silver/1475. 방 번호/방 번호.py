from collections import Counter
import sys
input = sys.stdin.readline

n = input()
arr = []

c = Counter(n)
num96 = 0
for x, cnt in c.items():
    if x == '9' or x == '6':
        num96+= cnt
    else:
        arr.append(cnt)

# 6 -> 3, 7 -> 4
if num96 > 0:
    to_add = num96//2 if num96%2 == 0 else num96//2+1
    arr.append(to_add)

print(max(arr))