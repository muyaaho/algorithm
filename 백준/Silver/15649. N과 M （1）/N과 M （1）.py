n, m = map(int, input().split())
arr = []

def func():
    if len(arr) == m:
        print(*arr)
        return
    for x in range(1, n+1):
        if x not in arr:
            arr.append(x)
            func()
            arr.pop()

func()
