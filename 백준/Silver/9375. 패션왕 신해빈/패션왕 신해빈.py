import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dict = {}
    n = int(input())
    if n == 0:
        print(0)
        continue
    for _ in range(n):
        a, b = input().rstrip().split()
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = [a]
    
    answer = 1
    for line in dict:
        answer *= (len(dict[line])+1)
        
    print(answer - 1)