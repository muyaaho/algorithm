from collections import Counter

n = list(input())
c = Counter(n)
odd = 0
on = ''
for x, cnt in c.items():
    if cnt%2 == 1:
        odd += 1
        on = x
    if odd > 1:
        print("I'm Sorry Hansoo")
        exit(0)

n.sort()
# print(n)
answer = ""
s = sorted(set(n))
for x in s:
    if c[x] > 1:
        answer += x*(c[x]//2)   
    # else:
    #     answer += x
if on != '':
    answer += on
    print(answer+answer[:-1][::-1])
else:
    print(answer + answer[::-1])