import sys
input = sys.stdin.readline
# 가장 인접한 두 공유기 사이의 거리를 최대로 만들기
n, c = map(int, input().split())

array = [] # 집의 좌표 저장할 리스트 초기화

# 각 집의 좌표 입력 >> 오름차순 정렬 - 정렬되어 있는 값만 이분탐색 가능
for _ in range(n):
    array.append(int(input()))
array.sort() 

start = 1 # 거리의 최솟값
end = array[-1] - array[0]  # 거리의 최댓값(첫 번째 집과 마지막 집 사이의 거리)
result = 0 # 가장 인접한 두 공유기 사이의 최대 거리를 저장

# 거리의 최소값과 최대값을 조정하며 탐색
while(start <= end):
    mid = (start + end) // 2  # 현재 탐색하는 거리의 중간
    value = array[0] #현재 거리로 공유기를 설치할 때, 마지막으로 공유기를 설치한 집의 좌표를 저장
    count = 1 # 설치한 공유기의 개수
	
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1, n):
        if array[i] >= value + mid: # 현재 집과 이전에 설치한 집 사이의 거리가 현재 거리 이상이면
            value = array[i] # 현재 집을 마지막으로 설치한 집
            count += 1 
    if count >= c:  # 현재 거리로 설치한 공유기의 개수가 목표 개수 c보다 크거나 같다면,
        start = mid + 1 # 거리의 최소값을 증가시켜 더 멀리 떨어진 공유기를 설치
        result = mid # 가장 인접한 두 공유기 사이의 최대 거리를 result에 저장
    else:  # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)