a, b = map(int, input().split())
ilist = list(map(int, input().split()))

end = a-1
max = 0

for i in range(end, 1, -1):
    for k in range(i-1, 0, -1):
        for p in range(k-1, -1, -1):
            sum = ilist[i]+ilist[k]+ilist[p]
            if sum <= b and max<sum:
                max = sum

print(max)
            

