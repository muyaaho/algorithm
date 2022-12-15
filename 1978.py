n = int(input())
answ = 0
inputlist = input().split()

for x in map(int, inputlist):
    count = 0
    #x = int(x)
    for k in range(1, x+1):
        if x%k == 0:
            count += 1
    
    if count == 2:
        answ += 1

print(answ)