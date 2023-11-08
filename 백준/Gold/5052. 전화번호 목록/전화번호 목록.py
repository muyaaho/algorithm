import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(input().rstrip() for _ in range(n)))
    isNo = False
    for i in range(n-1):
        if nums[i+1].find(nums[i]) == 0:
            isNo = True
            break
    print('NO' if isNo else 'YES')