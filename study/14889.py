import sys
# https://www.acmicpc.net/problem/14889

def calculate(n, ability, team1):
    team2 = list(set(range(n))-set(team1))
    team1_sum = 0
    for i, v1 in enumerate(team1[:-1]):
        for v2 in team1[i+1:]:
            team1_sum += ability[v1][v2] + ability[v2, v1]
    
    team2_sum = 0
    for i, v1 in enumerate(team2[:-1]):
        for v2 in team2[i+1:]:
            team2_sum += ability[v1][v2] + ability[v2][v1]
    
    ans.append(abs(team1_sum - team2_sum))
    return ans

def solution(n, ans):
   if len(ans) == n/2:
       calculate(n, ability, ans)

    for i in range(team[-1] if team else 0, n):
        if team and team[0] != 0:
            return None
        if i not in team:
            team.append(i)
            calculate(n, ability, team, )
            team.pop()


if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    ability = [list(map(int, read().split())) for _ in range(N)]
    ans = []
    answer = solution(N, ans)
    print(answer)
    