n = int(input())
m = int(input())
broken = set(input().split()) if m else set()
answer = abs(100-n)

# nums가 지금 나온 숫자(누른 리모컨 번호)
for nums in range(1_000_001):
    for num in str(nums):
        if num in broken:
            break
    else:
        # 버튼 누른 횟수 + 차이점(+, - 이동)
        answer = min(answer, len(str(nums)) + abs(nums-n))

print(answer)