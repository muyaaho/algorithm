import sys
input =sys.stdin.readline
def nqueen(depth):
    global answer
    if n == depth:
        answer += 1
        return
    
    for i in range(n):
        if not visited[i]:
            board[depth] = i
            
            if check(depth):
                visited[i] = True
                nqueen(depth+1)
                visited[i] = False

def check(n):
    for i in range(n):
        if (board[i] == board[n]) or (n-i == abs(board[i] - board[n])):
            return False
    return True


n = int(input())
board = [0] * (n+1)
visited = [False] * (n+1)
answer = 0
nqueen(0)

print(answer)