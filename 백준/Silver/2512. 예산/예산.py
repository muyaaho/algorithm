import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(arr)

if sum(arr) <= budget:
    print(end)
    exit(0)

ans = 0
while start <= end:
    mid = (start+end)//2
    # 모든 예산이 mid만큼 빼서 더한 값을 계산해야됨
    a = [x if x <= mid else mid for x in arr]
    s = sum(a)
    if s <= budget:
        start = mid + 1
        ans = mid
    else:
        
        end = mid - 1

print(ans)