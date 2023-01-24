n, k = map(int, input().split())
answer = []
arr = list(range(1, n+1))

idx = 0
while arr:
    size = len(arr)
    idx = (idx+(k-1))%size
    answer.append(arr[idx])
    del arr[idx]

print('<', end='')
print(*answer, sep=', ', end='')
print('>')