from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = []

for x in arr:
    # print(f'x: {x}')
    if not answer:
        answer.append(x)
    else:
        if answer[-1] < x:
            answer.append(x)
        else:
            idx = bisect_left(answer, x)
            answer[idx] = x
    
print(len(answer))