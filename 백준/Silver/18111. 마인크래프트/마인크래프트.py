import sys
input = sys.stdin.readline
from collections import Counter

n, m, b = map(int, input().split())
land = []
for _ in range(n):
    land += list(map(int, input().split()))

lm = max(land)
ln = min(land)

c = Counter(land)
# print(c)

time = 0
length = 0
a_time = 1e9
a_len = -1
    
for want in range(min(land), lm+1):
    # want 만큼 깎아서 나온 블록을 인벤토리에 집어넣기(뒤에서 2 곱하면 뺀 시간으로도 쓸 수 있음!)
    # 얹을 수 있는 경우도 같이 계산
    sub = 0 # 깎은 수
    add = 0 # 더할 수 있는 개수
    
    # want 하나 가지고 두 번 계산함 내가 원하는건 한 cnt를 이용해 sub와 add를 한 번에 구하는 것!
    for x, cnt in c.items():
        # 깎을 수 있으면
        if x - want > 0:
            sub += (x-want)*cnt
        elif x - want < 0:
            add += (want-x)*cnt
    
    # 인벤에 있는 블록 개수가 얹을 수 있는 개수라면 얹는 경우 시간 계산
    if add <= sub+b:
        # 시간 = 얹는 수 + 깎은 개수 *2
        time = add + sub*2
        length = want
    
    # 정답
    if a_time >= time:
        a_time = time
        a_len = length
    
print(a_time, a_len)