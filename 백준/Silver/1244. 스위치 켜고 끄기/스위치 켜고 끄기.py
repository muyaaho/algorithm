import sys
input = sys.stdin.readline

sn = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    s, n = map(int, input().split())
    if s == 1:  # 남자      
        for i in range(n-1,sn,n):
            switch[i] = 1-switch[i]

    else:       # 여자
        switch[n-1] = 1 - switch[n-1]
        right=n
        left =n-2
        while left >= 0 and right < sn: # 바꿀 구간 찾기
            # print(left, right)
            if switch[left] == switch[right]:
                switch[left] = 1-switch[left]
                switch[right] = 1-switch[right]
                right += 1
                left -= 1
            else:
                break
            

for i, x in enumerate(switch):
    if i != 0 and i%20 == 0:
        print()
    print(x, end=' ')