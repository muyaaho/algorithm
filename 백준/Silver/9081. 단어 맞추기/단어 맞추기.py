for _ in range(int(input())):
    a = list(input())
    n = len(a)
    m, k = 0,0
    # print(a)
    for idx in range(n-1):
        if a[idx] < a[idx+1]:
            k = idx
            
    for idx in range(k+1, n):
        if a[k] < a[idx]:
            m = idx
    # print('k, m:',k, m)
    if not(k==0 and m==0):
        a[k], a[m] = a[m], a[k]
        # print(a)
        a[k+1:] =  list(reversed(a[k+1:]))
        # print(a)
    print(''.join(a))
