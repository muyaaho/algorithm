'''
- 놀랍게도 정렬이 가능함 
- 정렬하고(내림차순) 제일 큰 수 부터 묶기
- 만약 음수 개수가 짝수개라면 곱해도 됨 + 0까지 ((-1, 0), 1)
- 같은 수가 있다면 1일 때 빼고 다 곱해(1일 때는 더하기)

- 어차피 정렬 가능하니까 음수~0 배열 1개, 양수 배열 1개 만들어서 음수는 오름차순으로 제일 작은 수 부터 곱하고
양수는 내림차순 해서 제일 큰 수 부터 묶기
'''


n = int(input())

parr = []
narr = []

for _ in range(n):
    x = int(input())
    if x > 0:
        parr.append(x)
    else:
        narr.append(x)

parr.sort(reverse=True)
narr.sort()

answer = 0

if parr and max(parr) == 1:
    answer += sum(parr)

elif len(parr) > 1:
    for i in range(0, len(parr), 2):
        if i+1 < len(parr):
            if parr[i] == 1 or parr[i+1] == 1:
                answer += parr[i]+parr[i+1]
            else:
                answer += parr[i]*parr[i+1]
        else:
            answer += parr[i]
else:
    answer += sum(parr)

if len(narr) > 1:
    for i in range(0, len(narr), 2):
        if i+1 < len(narr):
            answer += narr[i]*narr[i+1]
        else:
            answer += narr[i]
else:
    answer += sum(narr)

print(answer)