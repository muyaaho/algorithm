n, k = map(int, input().split())
l = []
answer = 0
for x in range(n):
    l.append(int(input()))

l = list(filter(lambda x : x<=k, l))
p = l[-1]
while k > 0:
    for x in l[::-1]:
        if k>=x:
            if p >x and len(l)>1:
                l.pop(-1)
                p = l[-1]
                #print(l)    
            answer += k//x
            k %= x
            
            #print(f'money: {k}, answer: {answer}')
            break

print(answer)