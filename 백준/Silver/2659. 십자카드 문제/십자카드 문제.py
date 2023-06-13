from collections import deque
from heapq import heappush, heappop

arr = list(map(int, input().split()))
nums = []

def t_num(arr):
    ans = []
    arr = deque(arr)
    for i in range(4):
        arr.rotate(1)
        n = int(''.join(map(str, arr)))
        heappush(ans, n)
    return heappop(ans)

flag = False
cnt = 0
all_nums = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if flag:
                    exit()
                arr2 = [a,b,c,d]
                a2 = t_num(arr2)
                if a2 not in all_nums:
                    all_nums.add(a2)
                    if t_num(arr) == a2:
                        print(cnt+1)
                        flag=True
                    else:
                        cnt += 1