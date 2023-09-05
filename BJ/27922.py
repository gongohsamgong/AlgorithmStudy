import sys


def two_subjects(lectures):
    communication_algorithm, algorithm_machine, machine_communication = [], [], []
    for lecture in lectures:
        communication_algorithm.append(lecture[0] + lecture[1])
        algorithm_machine.append(lecture[1] + lecture[2])
        machine_communication.append(lecture[2] + lecture[0])
    return communication_algorithm, algorithm_machine, machine_communication


def solution(comm_alg, alg_mach, mach_comm, k):
    comm_alg.sort(reverse=True)
    alg_mach.sort(reverse=True)
    mach_comm.sort(reverse=True)
    candidate = [sum(comm_alg[:k]), sum(alg_mach[:k]), sum(mach_comm[:k])]
    return max(candidate)


if __name__ == "__main__":
    read = sys.stdin.readline
    N, K = map(int, read().split())
    lectures = [list(map(int, read().split())) for _ in range(N)]
    communication_algorithm, algorithm_machine, machine_communication = two_subjects(lectures)
    ans = solution(communication_algorithm, algorithm_machine, machine_communication, K)
    print(ans)
