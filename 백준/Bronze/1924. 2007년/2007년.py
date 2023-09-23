m, d = map(int, input().split())
check = 0

for i in range(m):
    # print('i: ',i)
    if i in (1,3,5,7,8,10,12):
        check += 31
    elif i in (4,6,9,11):
        check += 30
    elif i == 2:
        check += 28
    # print(check)

check += d
mod = check % 7

# print(check, mod)
if mod == 1:
    print('MON')
elif mod == 2:
    print('TUE')
elif mod == 3:
    print('WED')
elif mod == 4:
    print('THU')
elif mod == 5:
    print('FRI')
elif mod == 6:
    print('SAT')
else:
    print('SUN')