for _ in range(int(input())):
    # 팀 개수, 문제개수, 우리 팀 id, 로그 개수
    n, k, t, m = map(int, input().split())
    
    # [0] idx: team_id, [1] idx: 문제 번호
    scores = [[0]*k for _ in range(n)]
    counts = [0]*n
    times = [0]*n
    
    for time in range(m):
        ti, pn, s = map(int, input().split())
        scores[ti-1][pn-1] = max(scores[ti-1][pn-1], s)
        counts[ti-1] += 1
        times[ti-1] = time
    
    # print('s\n', scores)
    # print('c\n', counts)
    # print('t\n', times)
    # index는 team id, [점수, count, 제출시간]
    ans = []
    for i in range(n):
        ans.append([i+1, sum(scores[i]), counts[i], times[i]])
    sd = sorted(ans, key=lambda x: (x[1], -x[2], -x[3]), reverse=True)

    for i, x in enumerate(sd):
        if x[0] == t:
            print(i+1)
            break