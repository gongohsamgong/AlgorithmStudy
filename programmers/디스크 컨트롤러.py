import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for request_time, cost_time in jobs:
            # 현재 처리 가능한 일을 heap에 넣기
            if start < request_time <= now:
                # 소요 시간이 작은 작업을 먼저 처리할 수 있도록
                heapq.heappush(heap, [cost_time, request_time])
        # 힙에 작업이 남아있는 한
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            # 일한 후의 시간 - 일 시작 시점의 시간 = 소요 시간
            answer += (now - current[1])
            # 다음 작업으로 이동
            i += 1
        else:
            # 그냥 일 진행중으로 1 시간만큼만 이동
            now += 1
    return int(answer / len(jobs))
