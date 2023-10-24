import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽ㅇ비
        heapq.heappush(q,(food_times[i], i+1))  
    
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재의 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous)*length
        length -= 1
        previous = now
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value) % length][1]