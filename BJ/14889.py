import sys


# 팀 능력치 계산 함수
def cal_diff(team1, team2, num):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(num):
        for j in range(num):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)


# 팀 구성 함수
def make_team(team1, count, n, start):
    global answer
    # 팀 능력치 차이 계산 시점: 팀 인원 반반일 때
    if count == n//2:
        team2 = []
        for i in range(n):
            if i not in team1:
                team2.append(i)
        print('team1 :', team1)
        print('team2 :', team2)

        diff = cal_diff(team1, team2, count)
        answer = min(answer, diff)
        return

    for i in range(start, n):
        if i not in team1:
            team1.append(i)
            # 팀내 인원수와 시작지점에 각각 하나를 더한 뒤 재귀함수
            make_team(team1, count+1, n, i+1)
            team1.remove(i)


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    arr = [list(map(int, read().split())) for _ in range(N)]
    answer = int(1e9)
    make_team([], 0, N, 0)
    print(answer)
    