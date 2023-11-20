import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(n):
    goal = arr[i]
    start = 0
    end = n-1
    
    while start < end:
        if arr[start] + arr[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                # print(goal, arr[start], arr[end])
                break
        elif arr[start] + arr[end] < goal:
            start += 1
        else:
            end -= 1
print(answer)