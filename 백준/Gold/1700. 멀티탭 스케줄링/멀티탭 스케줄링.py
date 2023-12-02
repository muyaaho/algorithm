import sys
input = sys.stdin.readline

n, k = map(int, input().split())
multitap = list(map(int, input().split()))

plugs = []
count = 0 

for i in range(k):
    # print(i, plugs)
    if multitap[i] in plugs:
        continue
    
    if len(plugs) < n:
        plugs.append(multitap[i])
        continue
    
    # 빼야 할 때
    multitap_idxs = []
    hasplug = True
    
    for j in range(n):
        if plugs[j] in multitap[i:]:
            idx = multitap[i:].index(plugs[j])
        else:
            idx = 101
            hasplug = False
        multitap_idxs.append(idx)
    
        if not hasplug:
            break
    
    plug_out = multitap_idxs.index(max(multitap_idxs))
    del plugs[plug_out]
    plugs.append(multitap[i])
    count += 1
    

print(count)