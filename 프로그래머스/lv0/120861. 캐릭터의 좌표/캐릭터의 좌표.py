def solution(keyinput, board):
    answer = [0,0]
    bw = board[0]//2
    bh = board[1]//2
    # input을 반복문을 돌려서 그 자리가 나올때마다 answer변화시키기
    # board는 맵 크기, 맵 크기를 반으로 나눈 수를 초과하면 반대쪽으로 가야 됨
    for comm in keyinput:
        if comm == "left":
            answer[0] -= 1
        elif comm == "right":
            answer[0] += 1
        elif comm == "up":
            answer[1] += 1
        else:
            answer[1] -= 1
        
        if answer[0] > bw:
            answer[0] = bw
        elif answer[0] < -bw:
            answer[0] = -bw
        if answer[1] > bh:
            answer[1] = bh
        elif answer[1] < -bh:
            answer[1] = -bh
        
    return answer