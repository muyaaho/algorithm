n, m = map(int,input().split())
ans = []

def func():
    if len(ans)==m:
        print(*ans)
        return
    for x in range(1,n+1):
        if x not in ans:
            ans.append(x)
            func()
            ans.pop()

func()  
