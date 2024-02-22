import sys
input = sys.stdin.readline

n, k = map(int, input().split())
multitap = list(map(int, input().split()))

plugs = []
count = 0
for i in range(k):
    if multitap[i] in plugs:
        continue
    
    if len(plugs) < n:
        plugs.append(multitap[i])
        continue
    
    multitap_idx = []
    hasplug = True
    
    for j in range(n):
        # 나중에 쓸 목록에 지금 플러그에 있는 것이 있다면
        if plugs[j] in multitap[i:]:
            idx = multitap[i:].index(plugs[j])
        else:
            idx = 101
            hasplug = False
        multitap_idx.append(idx)
        
        if not hasplug:
            break
    
    plugs_out = multitap_idx.index(max(multitap_idx))
    del plugs[plugs_out]
    plugs.append(multitap[i])
    count += 1

print(count)