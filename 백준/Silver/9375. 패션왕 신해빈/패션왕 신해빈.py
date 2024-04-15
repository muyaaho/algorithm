import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dict = {}
    for _ in range(n):
        a, b = input().rstrip().split()
        if b not in dict:
            dict[b] = [a]
            continue
        dict[b].append(a)
    
    answer = 1
    for key in dict:
        answer *= (len(dict[key]) + 1)

    print(answer - 1)