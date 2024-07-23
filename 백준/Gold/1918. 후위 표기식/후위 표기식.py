import sys
input = sys.stdin.readline

arr = list(input().rstrip())
stack = []
ans = ''

for x in arr:
    if x.isalpha():
        ans += x
        continue
    
    if x == ')':
        while stack and (stack[-1] != '('):
            ans += stack.pop()
        stack.pop()
        continue
    
    if x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            ans += stack.pop()
    
    if x == '+' or x == '-':
        while stack and (stack[-1] != '('):
            ans += stack.pop()
        
    stack.append(x)

    
while stack:
    ans += stack.pop()
print(ans)