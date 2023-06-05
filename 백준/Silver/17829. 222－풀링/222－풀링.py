import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def f(arr):
    if len(arr)==1:
        return arr[0][0]
    ans = []
    for x in range(0, len(arr)//2):
        ans.append([])
        for y in range(0, len(arr)//2):
            x2 = x*2
            y2 = y*2
            
            l1 = []
            l1.extend(arr[x2][y2:y2+2])
            l1.extend(arr[x2+1][y2:y2+2])

            l1.sort()
            ans[x].append(l1[2])
    return f(ans)
print(f(arr))