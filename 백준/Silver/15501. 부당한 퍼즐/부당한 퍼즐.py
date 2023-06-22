from collections import deque

n = int(input())
first = list(map(int, input().split()))
todo = list(map(int, input().split()))

q = deque(todo)

cnt = 0
flag = False
while cnt < 5:
    r_num = q.index(first[0])
    # print(cnt)
    # print(r_num)
    q.rotate(-r_num)
    # print('rotate: ', q)
    if list(q) == first:
        flag = True
        break
    q.reverse()
    # print('reverse: ',q)
    if list(q) == first:
        flag = True
        break
    cnt += 1

print('good puzzle' if flag else 'bad puzzle')