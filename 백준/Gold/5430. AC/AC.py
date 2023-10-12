import sys
input = sys.stdin.readline

def list_print(arr, is_reverse):
    if not arr:
        print('[]')
    else:
        if is_reverse:
            arr = list(reversed(arr))
        print('[' + ','.join(arr)+']')

for _ in range(int(input())):
    cmds = input()
    n = int(input())
    arr = input().rstrip().strip('[]').split(',')
    if '' in arr:
        arr = []
    
    is_error = False
    is_reverse = False
    
    for cmd in cmds:
        if cmd == 'R':
            is_reverse = not is_reverse
        elif cmd == 'D':    
            idx = -1 if is_reverse else 0
            try:
                arr.pop(idx)
            except:
                print('error')
                is_error = True
                break
    
    if not is_error:
        list_print(arr, is_reverse)  