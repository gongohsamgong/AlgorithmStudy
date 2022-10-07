from copy import deepcopy

# 최대 점수차
max_diff = 0
answer = []

# dfs를 이용한 완전탐색 - 라이언이 화살쏘는것
def dfs(apeach, ryan, n, i):
    global answer, max_diff
    if i == 11: # 화살 다 쐈으면
        if n != 0:  # 쏜 화살 수
            ryan[10] = n    # 0점에 화살을 쏜다.
        score_diff = calcDiff(apeach, ryan)
        if score_diff <= 0:     # 어피치와 라리언이 점수가 같거나 어피치가 더 높은 점수인 경우, 라이언은 선택지가 없음
            return
        result = deepcopy(ryan) # 라이언 점수가 더 높다, 이러면 점수 후보지에 들어가므로 deepcopy한다
        if score_diff > max_diff:   # 점수 차이가 가장 크다면
            max_diff = score_diff
            answer = [result]   # 갱신. answer는 값 하나만 들고 있는거임
            return

        if score_diff == max_diff:  # 최고 점수차가 같다면 이제 낮은 점수에 분포되어있는거 골라야되니까 갱신이 아니라 추가.
            answer.append(result)

    if apeach[i] < n:   # 라이언이 쏠수 있는 화살수가 apeach가 현재 점수에 쏜 화살수보다 많이 남았을때
        ryan.append(apeach[i] + 1)  # 어피치가 쏜것보다 하나만 더 많아도 충분. greedy
        dfs(apeach, ryan, n-apeach[i]-1, i+1)   # 횟수가... 라이언이 어피치보다 하나 더 쐈으니 -1 또 하는겨. i+1인 이유는 다음 점수란에서 봐야되니까.
        ryan.pop()  # 어.. 만약 정답이면 이미 위에서 answer가 정해졌을 것. 근데 아니므로 위에 dfs를 돌렸음에도 아래 칸으로 온거니까 실패작. 그러므로 ryan은 안쏜걸로 해야하므로 pop

    # 현재 점수대에 화살을 쏘지 않는 경우
    ryan.append(0)  # 해당 점수칸에 횟수 0
    dfs(apeach, ryan, n, i+1)
    ryan.pop()


def calcDiff(apeach, ryan):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (apeach[i], ryan[i]) == (0, 0):
            continue
        if apeach[i] > ryan[i]:     # 어피치가 횟수가 높았을 때
            enemyScore += (10 - i)  # 어피치쪽 점수 획득
        else:
            myScore += (10 - i)

        return myScore - enemyScore     # 라이언 - 어피치

def solution(n, info):
    global answer, max_diff
    dfs(info, [], n, 0)
    if answer == []:
        return [-1]
    answer.sort(key=lambda x: x[::-1], reverse=True)    # 최대 점수차가 나오는 배열을 낮은 점수에 화살이 많은 순으로 sort
    return answer[0]