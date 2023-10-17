import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    
    arr.sort()
    a = arr[0][1]
    answer = 1
    
    for x, y in arr[1:]:
        if y < a:
            answer += 1
            a = y
    
    print(answer)