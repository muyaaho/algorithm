from collections import deque
from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
d = {}
# + - * /

# print(oper)
opers = [i for i, x in enumerate(oper) for _ in range(x)]

# print(list(permutations(opers, len(opers))))
# print(opers)

ans = []
for pmts in set(permutations(opers, len(opers))):
    result = nums[0]
    for i, x in enumerate(pmts):
        if x == 0:
            result += nums[i+1]
        elif x == 1:
            result -= nums[i+1]
        elif x == 2:
            result *= nums[i+1]
        elif x == 3:
            result = int(result / nums[i+1])
    ans.append(result)
    # print(list(pmts), result)

print(max(ans))
print(min(ans))