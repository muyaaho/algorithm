import sys
from collections import deque

deck = deque()
for _ in range(int(input())):
    cmd = list(map(int, sys.stdin.readline().split()))
    
    if cmd[0] == 1:
        deck.appendleft(cmd[1])
    elif cmd[0] == 2:
        deck.append(cmd[1])
    elif cmd[0] == 3:
        print(deck.popleft() if deck else -1)
    elif cmd[0] == 4:
        print(deck.pop() if deck else -1)
    elif cmd[0] == 5:
        print(len(deck))
    elif cmd[0] == 6:
        print(0 if deck else 1)
    elif cmd[0] == 7:
        print(deck[0] if deck else -1)  
    elif cmd[0] == 8:
        print(deck[-1] if deck else -1)
