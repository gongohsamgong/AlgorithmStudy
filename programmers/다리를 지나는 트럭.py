"""
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:

        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return answer
"""

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0

    while len(truck_weights) != 0:
        answer += 1
        current_weight -= bridge.popleft()

        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            current_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

    answer += bridge_length
    return answer
