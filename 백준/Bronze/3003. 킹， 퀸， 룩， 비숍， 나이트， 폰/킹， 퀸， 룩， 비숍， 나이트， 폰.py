a = list(map(int, input().split()))
answer = []

for i, x in enumerate(a):
    if i==0 or i==1:
        answer.append(1-x)
    elif i==2 or i==3 or i==4:
        answer.append(2-x)
    else:
        answer.append(8-x)
print(*answer)