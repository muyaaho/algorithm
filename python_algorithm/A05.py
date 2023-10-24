n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0]*11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n

print(result)