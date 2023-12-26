s, k = map(int, input().split())

arr = [s//k for _ in range(k)]

for i in range(s%k):
    arr[i] += 1

answer = 1

for x in arr:
    answer *= x

print(answer)