n = int(input())
arr = {input() for _ in range(n)}

arr = sorted(arr)
arr = sorted(arr, key=lambda x: (len(x)))

print(*arr, sep='\n')