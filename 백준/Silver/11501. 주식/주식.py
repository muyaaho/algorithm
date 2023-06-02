import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.reverse()
    max = arr[0]
    ans = 0
    
    for x in arr[1:]:
        if max < x:
            max = x
            continue
        ans += max-x
    
    print(ans)