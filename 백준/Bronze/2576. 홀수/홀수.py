arr = [int(input()) for _ in range(7)]
arr = [i for i in arr if i%2 == 1]

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)