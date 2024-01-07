n,m = map(int, input().split())
arr = sorted(map(int, input().split()))

def dfs(cnt, nums):
    if cnt == m:
        print(*nums)
        return
    
    for i in arr:
        if not i in nums:
            nums.append(i)
            # print(i, nums)
            dfs(cnt + 1, nums)
            nums.pop()

for i in arr:
    dfs(1, [i])