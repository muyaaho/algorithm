n = int(input())
arr = []
for x in range(n):
    arr.append(list(map(int, input().split())))
b,w = 0,0

def check(a):
    global b,w
    
    cntb,cntw=0,0
    for x in a:
        # print(x)
        if 0 not in x:
            cntb += 1
        elif 1 not in x:
            cntw += 1

    if cntb == len(a):
        b += 1
        return
    elif cntw == len(a):
        w += 1
        return

    div = len(a)
    
    check([row[0:div//2] for row in a[0:div//2]])
    check([row[0:div//2] for row in a[div//2:div]])
    check([row[div//2:div] for row in a[0:div//2]])
    check([row[div//2:div] for row in a[div//2:div]])
    
check(arr)
print(w)
print(b)