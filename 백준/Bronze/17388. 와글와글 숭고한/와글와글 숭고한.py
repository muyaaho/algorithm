arr = list(map(int, input().split()))
dic = {0:'Soongsil', 1:'Korea', 2:'Hanyang'}
sname = {x:i for i, x in enumerate(arr)}

if sum(arr)>= 100:
    print('OK')
else:
    arr.sort()
    print(dic[sname[arr[0]]])