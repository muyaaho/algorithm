a, b = input().split()

cnt = 0
while True:
    # print(a, b)
    if a == b:
        print(cnt+1)
        break
    try:
        if b[-1] == '1':
            b = b[:-1]
        elif int(b)%2 == 0: 
            b = str(int(b)//2)
        else:
            print(-1)
            break
    except:
        print(-1)
        break
    cnt += 1