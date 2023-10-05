n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n

now = 0 # 지금 있는 곳
togo = arr[0]   # 갈 곳
visited[0] = True
print(1,end=' ')

# 방문하지 않은 곳이 있다면(모두 True가 될 때 까지)
while False in visited:
    # 오른쪽으로 한 칸씩 이동
    if togo > 0:
        while togo>0:
            # 한 칸 이동
            togo -= 1
            now = (now+1)%n
            while visited[now]:
                now = (now+1)%n
        
    # 왼 쪽으로 한 칸씩 이동
    else:
        while togo<0:
            togo += 1
            now = (now-1+n)%n
            while visited[now]:
                now = (now-1+n)%n
    visited[now] = True
    print(now+1, end=' ')
    togo = arr[now]