from collections import deque

while True:
    a = input()
    if a == ".":
        break
    
    a = "".join(a.split())
    q = deque()
    for x in a:
        if x == "(" or x == "[":
            # print(x, q)
            q.append(x)
        elif x == ")":
            # print(x, q)
            if len(q) > 0 and q[-1] == "(":
                q.pop()
            else:
                q.append(x)
        elif x == "]":
            # print(x, q)
            if len(q) > 0 and q[-1] == "[":
                q.pop()
            else:
                q.append(x)
    print("yes" if len(q) == 0 else "no")