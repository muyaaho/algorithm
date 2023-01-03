time = int(input())
button = [300, 60, 10]
answer = [0,0,0]

for i, t in enumerate(button):
    if time >= t:
        answer[i] += time//t
        time %= t

if time > 0:
    print(-1)
else:
    print(*answer)