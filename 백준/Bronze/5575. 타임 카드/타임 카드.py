for _ in range(3):
    goh, gom, gos, geth, getm, gets = map(int, input().split())
    h = geth-goh
    m = getm-gom
    s = gets-gos

    if s<0:
        m -= 1
        s += 60
    if m<0:
        h -= 1
        m += 60

    print(h, m, s)