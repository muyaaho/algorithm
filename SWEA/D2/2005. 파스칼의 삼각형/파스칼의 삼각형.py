T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[1]*(x+1) for x in range(n)]

    
    for i, line in enumerate(arr):
        for j, x in enumerate(line):
            if not(j == 0 or j == i):
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    
    print(f"#{test_case}")
    for line in arr:
        print(*line)