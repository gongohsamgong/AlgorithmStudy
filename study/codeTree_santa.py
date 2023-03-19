import sys
from collections import defaultdict
MAX_M = 10

n, m, q = -1, -1, -1

# id별로 상자 무게 저장하는 딕셔너리
weight = {}

# id에 해당하는 상자의 이전, 다음 상자 정보
pre, nxt = defaultdict(lambda: 0), defaultdict(lambda: 0)

# 각 벨트별로 head, tail id 저장
head = [0] * MAX_M
tail = [0] * MAX_M

# 벨트의 고장 여부
broken = [False] * MAX_M

# 물건 별로 벨트 번호
belt_num = defaultdict(lambda: -1)


def build_factory(elem):    # 100 n m ID1 ID2 ... IDn W1 W2 ... Wn
    global n, m
    
    n, m = elem[1], elem[2]
    ids, weights = elem[3:3+n], elem[3+n, 3+2*n]
    
    for i in range(n):
        weight[ids[i]] = weights[i]
    
    # 벨트별로 상자 목록 넣기 n: 개수, m: 벨트 수
    size = n // m
    for i in range(m):
        head[i] = ids[i * size]
        tail[i] = ids[(i+1) * size - 1]


if __name__ == '__main__':
    read = sys.stdin.readline
    q = int(read())
    n, m = -1, -1
    for _ in range(q):
        elements = list(map(int, read().split()))
        q_type = elements[0]
        
        if q_type == 100:
            build_factory(elements)
        elif q_type == 200:
            drop_off(elements)
        elif q_type == 300:
            remove(elements)
        elif q_type == 400:
            find(elements)
        else:
            broken_belt(elements)
        
    
    