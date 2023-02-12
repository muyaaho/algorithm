import sys
input = sys.stdin.readline
n = int(input())

ans = 666
count = 0   # 666이 나왔을 때 count+1
while True:
    if '666' in str(ans):
        count += 1
    if count == n:  # count 해서 n과 같아지면 ans print
        print(ans)
        break
    ans += 1