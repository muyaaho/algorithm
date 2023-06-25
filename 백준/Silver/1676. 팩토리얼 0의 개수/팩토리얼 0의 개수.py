n = int(input())

if n == 0:
    print(0)
else:
    ans_int = 1
    for i in range(1, n+1):
        ans_int *= i
    s = str(ans_int)
    
    # print(s)
    # print(s[::-1])
    
    cnt = 0
    for x in s[::-1]:
        if x == '0':
            cnt += 1
        else:
            break
    print(cnt)