from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    
    q = deque()
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = arr[i-1]
    
    while q:
        now = q.popleft()
        
        for next in graph[now]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[now]+arr[next-1])
            if indegree[next] == 0:
                q.append(next)
    
    print(dp[w])