import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()

stack = []
for x in s:
    while stack and stack[-1] < x and k > 0:
        stack.pop()
        k -= 1
    stack.append(x)

print(''.join(stack[:-k]) if k > 0 else ''.join(stack))