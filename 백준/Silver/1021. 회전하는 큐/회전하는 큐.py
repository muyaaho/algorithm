from collections import deque

# 큐의 크기, 뽑아내려고 하는 수
n, m = map(int, input().split())

# 뽑아내려고 하는 수의 위치가 순서대로 주어짐
want = list(map(int, input().split()))

arr = deque(range(1, n+1))

answer = 0
for x in want:
    idx = arr.index(x)
    
    if idx > len(arr)//2:
        answer += (len(arr) - idx)
    else:
        answer += idx
    arr.rotate(-idx)
    # print(arr)
    arr.popleft()
    
print(answer)