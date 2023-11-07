arr = [int(input()) for _ in range(8)]
maparr = {x:i for i, x in enumerate(arr, start=1)}

arr.sort(reverse=True)

print(sum(arr[:5]))
print(*sorted([maparr[x] for x in arr[:5]]))