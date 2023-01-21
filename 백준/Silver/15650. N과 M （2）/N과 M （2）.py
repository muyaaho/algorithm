n, m = map(int, input().split())
arr = []

def f(start):
    if len(arr) == m:
        print(*arr)
        return

    for x in range(start, n+1):
        arr.append(x)
        f(x+1)
        arr.pop()

f(1)