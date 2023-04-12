import sys
input = sys.stdin.readline

q= [0]*5
for _ in range(int(input())):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        q[0] += 1
    elif x < 0 and y > 0:
        q[1] += 1
    elif x < 0 and y < 0:
        q[2] += 1
    elif x > 0 and y < 0:
        q[3] += 1
    else:
        q[-1] += 1

for i, x in enumerate(q, start = 1):
    if i == 5:
        print(f'AXIS: {x}')
    else:
        print(f'Q{i}: {x}')