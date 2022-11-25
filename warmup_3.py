def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if id_pw[0] == db[i][0]:    # 아이디가 같을 경우
            answer = "wrong pw"
            if id_pw[1] == db[i][1]:    # 비밀번호도 같을 경우
                answer = "login"
            return answer
        else:
            answer = "fail" # 아이디부터 안같을 경우
    return answer
