data = input()

def changeX(x):
    stra = 'A' * (len(x)//4) * 4
    strb = 'B' * (len(x)%4)
    return stra + strb

answer = -1

now = data[0]
if now == 'X':
    xarr = data[0]
    oarr = ''
else:
    xarr = ''
    oarr = '.'

isPosible = True
answer = ''
for x in data[1:]:
    if now == 'X':
        if now == x:
            xarr += x
        elif x == '.':
            now = '.'
            if len(xarr) % 2 == 1:
                isPosible = False
                break
            answer += changeX(xarr)
            xarr = ''
            oarr += '.'
    elif now == '.':
        if now == x:
            oarr += x
        elif x == 'X':
            now = 'X'
            answer += oarr
            oarr = ''
            xarr += 'X'
    # print(f'now: {now}, x: {x}')
    # print('xarr:', xarr)
    # print('oarr:',oarr)
    # print(answer)

if not isPosible:
    print(-1)

elif xarr:
    if len(xarr) % 2 == 1:
        print(-1)
    else:
        answer += changeX(xarr)
        print(answer)
elif oarr:
    answer += oarr
    print(answer)
else:
    print(answer)