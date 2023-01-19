while True:
    if (a:=input()) == '0':         # 바다코끼리 연산
        break

    mid = len(a)//2
    count = 0
    for i in range(mid):
        if a[i] == a[len(a)-i-1]:
            count += 1
    
    print('yes' if count == mid else 'no')