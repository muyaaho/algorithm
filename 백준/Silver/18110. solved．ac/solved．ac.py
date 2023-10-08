import sys

n = int(sys.stdin.readline())
scores = []
for _ in range(n):
    scores.append(int(sys.stdin.readline()))
scores.sort()

if n == 0:
    print(0)
else:
    peoples = n*0.15
    
    if peoples - int(peoples) >= 0.5:
        peoples = int(peoples) + 1
    else:
        peoples = int(peoples)

    # print(n, peoples)
    if peoples == 0:
        avg = sum(scores)/n
    else:
        avg = sum(scores[peoples:-peoples])/(n-2*peoples)
    print(int(avg)+1 if avg - int(avg) >= 0.5 else int(avg))