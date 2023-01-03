menu = [int(input()) for _ in range(5)]

hambuger = menu[:3]
drink = menu[3:]
s = []

print(min([i+j-50 for i in hambuger for j in drink]))