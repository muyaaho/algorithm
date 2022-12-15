word_n = int(input())
anw = 0
for k in range(word_n):
    count = 0
    word = input()
    check = []

    for ch in word:
        if not ch in check:
            check.append(ch)
        else:
            if check.index(ch) != len(check)-1:
                count += 1
                break
    
    if count == 0:
        anw += 1

print(anw)