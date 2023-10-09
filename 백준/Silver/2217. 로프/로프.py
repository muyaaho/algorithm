n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)

answer = 0
for i, x in enumerate(arr, start=1):
    tmp = x*i
    answer = max(answer, tmp)

print(answer)