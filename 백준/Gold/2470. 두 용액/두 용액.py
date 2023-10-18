import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = len(arr)-1

check = abs(arr[left] + arr[right])
a_l, a_r = arr[left], arr[right]
while left < right:
    l = arr[left]
    r = arr[right]

    if abs(l+r) < check:
        check = abs(l+r)
        a_l, a_r = l, r
    
    if l+r == 0:
        break
    # -99 -2 -1 4 98
    elif l + r < 0:
        left += 1
    else:
        right -= 1

print(a_l, a_r)