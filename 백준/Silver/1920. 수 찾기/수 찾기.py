n = int(input())
narr = set(map(int,input().split()))
m = int(input())
marr = list(map(int,input().split()))

for x in marr:
    if x in narr:
        print(1)
    else:
        print(0)    