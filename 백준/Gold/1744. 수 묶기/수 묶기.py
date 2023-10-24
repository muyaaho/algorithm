n = int(input())

parr = []
narr = []

for _ in range(n):
    x = int(input())
    if x > 0:
        parr.append(x)
    else:
        narr.append(x)

parr.sort(reverse=True)
narr.sort()

answer = 0

if parr and max(parr) == 1:
    answer += sum(parr)

elif len(parr) > 1:
    for i in range(0, len(parr), 2):
        if i+1 < len(parr):
            if parr[i] == 1 or parr[i+1] == 1:
                answer += parr[i]+parr[i+1]
            else:
                answer += parr[i]*parr[i+1]
        else:
            answer += parr[i]
else:
    answer += sum(parr)

if len(narr) > 1:
    for i in range(0, len(narr), 2):
        if i+1 < len(narr):
            answer += narr[i]*narr[i+1]
        else:
            answer += narr[i]
else:
    answer += sum(narr)

print(answer)