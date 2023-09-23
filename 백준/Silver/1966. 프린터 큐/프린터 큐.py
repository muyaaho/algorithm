from collections import deque

for x in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    tfarr = [False for _ in range(n)]
    # print(tfarr)
    tfarr[m] = True
    tfq = deque(tfarr)
    sarr = sorted(arr, reverse=True)
    # sq = deque(sarr)
    
    answer = 0
    q = deque(arr)
    
    idx = 0
    while q:
        idx %= n
        if sarr[idx] == q[0] and tfq[0] == True:
            print(answer + 1)
            break
        else:
            if sarr[idx] == q[0]:
                answer += 1
                idx += 1
                q.popleft()
                tfq.popleft()
            else:
                tfq.rotate(-1)
                q.rotate(-1)