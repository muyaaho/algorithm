import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = n

while start <= end:
    q = (start + end)//2
    
    if q ** 2 >= n:
        end = q-1
    else:
        start = q+1
if end ** 2 == n:
    print(end)
else:
    print(end+1)