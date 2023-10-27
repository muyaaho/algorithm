import sys
input = sys.stdin.readline
n = int(input())
stack = []
answer = []
isBreak = False

arr = [int(input()) for _ in range(n)]

num = 1
for x in arr:
    if isBreak:
        break
    while num <= x:
        stack.append(num)
        num += 1
        answer.append('+')
    
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        isBreak = True
        break
# print(isBreak)
if not isBreak:
    print(*answer, sep='\n')