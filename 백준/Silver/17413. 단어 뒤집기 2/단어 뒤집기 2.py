s = input()

angles = ""
blank = 0
word = ""
answer =[]
isAngle = False
isBlank = False
for x in s:

    if isAngle:
        if x == '>':
            isAngle = False
            angles += x
            answer.append(angles)
            angles = ""
            continue
        angles += x
        continue
    if isBlank:
        if x != ' ':
            if blank > 0:
                answer.append(" "*blank)
                blank = 0
            word += x
            isBlank = False
            continue
        blank += 1
        continue
    
    if x == '<':
        if word:
            answer.append(word[::-1])
            word = ""
        isAngle = True
        angles += x
        continue
    
    
    if x == ' ':
        if word:
            answer.append(word[::-1])
            word = ""
        isBlank = True
        blank += 1
        continue
    
    word += x
if word:
    answer.append(word[::-1])

print("".join(answer))