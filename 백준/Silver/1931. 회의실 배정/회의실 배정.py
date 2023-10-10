import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, reverse=True)
# print(arr)
# for문을 돌면서 조건에 맞으면 answer += 1
answer = 1
ck = arr[0][0]
for start, end in arr[1:]:
    if ck >= end:
        # print(ck, end)
        answer += 1
        ck = start

print(answer)