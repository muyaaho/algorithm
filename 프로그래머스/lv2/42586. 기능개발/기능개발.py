def solution(progresses, speeds):
    answer = []

    left = [0]*(len(progresses))
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        if (a:=(100-p)/s)%1 > 0:
            left[i] += 1
        left[i] += (100-p)//s

    stack = []
    for x in left:
        if not stack:
            stack.append(x)
        elif stack[0] >= x:
            stack.append(x)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(x)
    if stack:
        answer.append(len(stack))
            
    return answer