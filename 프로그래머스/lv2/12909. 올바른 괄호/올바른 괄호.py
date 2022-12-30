from collections import deque

def solution(s):
    answer = True
    queue = deque()
    queue.append(s[0])
    for x in s[1:]:
        if not queue and x == ")":
            return False
        elif x == ")" and queue[-1] == "(":
            queue.pop()
        else:
            queue.append(x)
        # print(f'x: {x}, queue: {queue}')
    
    if not queue:
        return True
    else:
        return False
    
# print(solution("()()"))
# print(solution("(())()"))
# print(solution(")()("))
# print(solution("(()("))
# print(solution("()())(()"))