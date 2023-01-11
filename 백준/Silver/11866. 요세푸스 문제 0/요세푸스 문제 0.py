n, k = map(int, input().split())

arr = list(range(1, n+1))
answer = []

i = k-1
while arr:
    answer.append(arr[i])
    if len(arr)==1:
        break
    arr.pop(i)
    i += (k-1)
    i %= len(arr)

print('<', end ='')
print(*answer, sep=', ', end='')
print('>', end ='')