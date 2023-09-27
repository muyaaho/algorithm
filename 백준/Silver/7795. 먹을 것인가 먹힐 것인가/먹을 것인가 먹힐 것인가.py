from bisect import bisect

for i in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    
    cnt = 0
    for ax in a:
        cnt += (bisect(b, ax-1))
    print(cnt)