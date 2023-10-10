n = int(input())
# [알파벳 인덱스, 가중치]
str_map = [[chr(ord('A')+x), 0] for x in range(26)]
in_arr = []

for _ in range(n):
    a = input()
    in_arr.append(a)
    for i, x in enumerate(a):
        idx = ord(x)-ord('A')
        str_map[idx][1] += (10**(len(a)-i))

str_map = sorted(str_map, key=lambda x: -x[1])
# print(str_map[:10])

# str_map을 반복하면서 a를 replace 시키기
idx = 0
change_num = 9
while str_map[idx][1] > 0:
    in_arr = [x.replace(str_map[idx][0], str(change_num)) for x in in_arr]
    change_num -= 1
    idx += 1

# print(in_arr)
in_arr = list(map(int, in_arr))
print(sum(in_arr))