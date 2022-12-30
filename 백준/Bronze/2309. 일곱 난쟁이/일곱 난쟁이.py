arr = [int(input()) for _ in range(9)]
check=[]

def func():
    # print(check)
    if len(check)==7:
        if sum(check)==100:
            for x in sorted(check):
                print(x)
            exit()
        return
    
    for x in arr:
        if x not in check:
            check.append(x)
            func()
            check.pop()

func()