T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    # N(2 ≤ N ≤ 1,000,000)
    arr = list(map(int, input().split()))
    
    sells = []
    price = -1

    for x in reversed(arr):
        if price < 0:
            price = x
        elif price > x:
            sells.append(price-x)
        else:
            price = x
        #print(x, sells)

    print(f"#{test_case} {sum(sells)}")
    
    
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
        뒤에서 부터 봤을 때 작으면 담아두고 커지면 담아뒀던거 팔고 가격 책정
        

            
    '''
    # ///////////////////////////////////////////////////////////////////////////////////
