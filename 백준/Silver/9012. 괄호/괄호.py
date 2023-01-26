import sys
input = sys.stdin.readline


for _ in range(int(input())):
    flag = False
    a = input().rstrip()
    stack = []
    for x in a:
        if x == '(':
            stack.append(x)
        else:
            try:
                stack.pop()
            except:
                flag = True
                break
            
    if not stack and not flag:
        print("YES")
    elif flag:
        print("NO")
    else:
        print('NO')


