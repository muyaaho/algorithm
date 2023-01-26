def solution(phone_book):
    phone_book.sort()
    
    for i, x in enumerate(phone_book[:-1], start = 1):
        if phone_book[i].find(x) == 0:
            return False
    return True