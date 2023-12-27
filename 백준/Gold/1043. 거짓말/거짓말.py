def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 사람 수, 파티 수
n, m = map(int, input().split())

# 진실을 아는 사람의 수와 번호 (수, 리스트)
truth = list(map(int, input().split()))

parent = list(range(n+1))

if truth[0] == 0:
    print(m)
    exit(0)

parties = [list(map(int, input().split())) for _ in range(m)]
for _ in range(m):
    for party in parties:
        # 파티에 있는 사람들을 묶음
        n = party[0]
        party = party[1:]
        party.sort()
        for p in party[1:]:
            if find_parent(parent, party[0]) != find_parent(parent, p):
                union_parent(parent, party[0], p)

answer = 0
# 파티를 돌아
for party in parties:
    party = party[1:]
    
    # 파티 사람의 부모와 truth의 부모가 같은지 확인
    cnt = 0
    for p in party:
        for t in truth[1:]:
            if parent[p] == parent[t]:
                cnt += 1
                break
    
    if cnt == 0:
        answer += 1
# print(parent)
print(answer)