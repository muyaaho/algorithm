import sys
input = sys.stdin.readline

stack = []
cnt = 1
answer = []
for _ in range(int(input())):
    n = int(input())

    # 꼭 stack[-1]로 안해도 됨! cnt가 있음
    while cnt <= n:
        stack.append(cnt)
        cnt += 1
        answer.append('+')

    if stack[-1] == n:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print(*answer, sep='\n')