import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    rarr = [0] * n
    left, right = 0, n-1
    
    for i in range(n):
        if i % 2 == 0:
            rarr[left] = arr[i]
            left += 1
        else:
            rarr[right] = arr[i]
            right -= 1
    
    answer = 0
    for i in range(n):
        if i == n-1:
            answer = max(answer, rarr[i]-rarr[0])
        else:
            answer = max(answer, abs(rarr[i+1]-rarr[i]))
    
    print(answer)