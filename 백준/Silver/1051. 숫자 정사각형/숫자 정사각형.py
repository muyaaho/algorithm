import sys
input = sys.stdin.readline

def find_same(x, y, size):
    if arr[x][y] == arr[x+size][y] == arr[x][y+size] == arr[x+size][y+size]:
        return True
    return False

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
nx = min(n, m)
answer = 1

def solution():
    global answer
    for i in range(n):
        for j in range(m):
            for size in range(nx, 0, -1):
                if 0 <= i + size < n and 0 <= j + size < m and find_same(i, j, size):
                    answer = max(answer, (size+1) ** 2)
                    break

solution()
print(answer)