def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    # 주어진 문제들의 max 알고력과 max 코딩력을 변수에 저장.
    for i in range(len(problems)):
        max_alp = max(problems[i][0], max_alp)
        max_cop = max(problems[i][1], max_cop)

    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    # 우선 생각할 수 있는 가장 큰 시간값을 변수에 저장한 뒤, 이를 dp 배열의 값으로 초기화.
    max_cost = 100 * (max_alp + max_cop)
    # 알고력, 코딩력이 max 값을 넘어서면 인덱스 에러가 발생하므로 max 값에 맞추어 dp 배열 생성.
    dp = [[max_cost + 1 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    # 기존에 주어진  알고력, 코딩력으로는 당장 문제를 풀 수 있으므로 시간 소요가 0이다. 따라서 dp에 0 값을 저장.
    dp[alp][cop] = 0
    # 현재 알고력, 코딩력부터 problems에서 제시된 max 알고력 코딩력까지 for문으로 순환하며 min 시간을 판별.
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 시작을 기존 알고력, 코딩력으로 했기에 1을 더해가면서 max 알고력, 코딩력보다 작을때까지 dp 비교.
            if i + 1 <= max_alp:
                # 당연히 최소 시간(cost)가 원하는 답이므로, 기존 i, j값에서 1을 더했을때 기존 dp 배열에서 시간 1을 더하는게 더 적은지,
                # 1 큰 알고력을 위해 필요한 시간이 더 적은지 비교
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            # 모든 problems에 대해 반복문을 돌리며 비교.
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # i, j에서 알고력 보상과 코딩력 보상으로 갈 수 있는 위치를 next에 저장.
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    # 문제를 모두 풀었을 때의 시간이 최종 답이 되므로 끝에 있는 값을 리턴.
    answer = dp[-1][-1]
    return answer