def solution(id_pw, db):
    i, p = id_pw

    if id_pw in db:
        return "login"
    for di, dp in db:
        if di == i:
            return "wrong pw"
    return "fail"