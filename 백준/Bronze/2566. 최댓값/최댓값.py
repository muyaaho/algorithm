arr = [list(map(int, input().split())) for x in range(9)]

m = {}
for x, line in enumerate(arr, start = 1):
    m[max(line)] = (x, line.index(max(line))+1)

print(max(m))    
print(*m[max(m)])