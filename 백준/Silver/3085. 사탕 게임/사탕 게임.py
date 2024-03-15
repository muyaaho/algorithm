'''
색이 다른 인접한 두 칸을 고르는 모든 경우의 수를 구함
한 번만 색상 변경
그리고 그 중에서 가장 긴 연속 부분인 행 or 열의 사탕 개수
'''

import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

answer = 0

def check():
    global answer
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1
                


for i in range(n):
    for j in range(n):
        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

print(answer)