l = list(map(int, input().split()))
s= set(l)
if len(s) == 3:
    print(max(s)*100)
elif len(s) == 2:
    for x in s:
        if l.count(x) == 2:
            print(1000+x*100)
else:
    print(10000+l[0]*1000)
    