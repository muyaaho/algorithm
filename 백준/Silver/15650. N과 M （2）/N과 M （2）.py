n, m = map(int, input().split())
arr = []

def f():
    if len(arr)==m:
        print(*arr)
        return
    
    for x in range(1, n+1):
        if not arr:
            arr.append(x)
            f()
            arr.pop(-1)
        elif arr[-1] < x:
            arr.append(x)
            f()
            arr.pop(-1)
            
f()