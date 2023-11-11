n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

end = arr[0] - 0.5 + l
answer = 1
for x in arr[1:]:
    if x > end:
        end = x-0.5+l
        answer += 1

print(answer)