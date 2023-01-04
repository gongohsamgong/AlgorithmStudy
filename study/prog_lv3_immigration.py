def solution(n, times):
    answer = 0
    # 이분탐색 사용, 백준 2512 참고
    start = min(times)  # 최소 시간: 최소 한명을 심사하는시간
    end = max(times) * n  # 최대 시간: 가장 오래 걸리는 심사대에서 모두가 입국심사 받는 경우
    while start <= end:
        mid = (start + end) // 2  # 한 심사관에게 주어진 시간
        ppl = 0  # 심사 완료한 사람 수
        for time in times:
            ppl += mid // time
            # 모든 사람을 심사했을 경우 for문 빠져나가기
            if ppl >= n:
                break
        # 현재 mid 값으로 충분히 심사가능하다면
        if ppl >= n:
            answer = mid
            end = mid - 1  # 더 작은 mid값으로 되는지 이분탐색
        else:
            start = mid + 1  # 더 큰 mid값으로 재도전

    return answer
