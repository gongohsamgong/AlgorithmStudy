import sys


def check():
    if

def match(p, m, players):
    rooms = []  # [10, [[10, a], [15, b]]] 입장기준 10인 방에 플레이어 두명
    ind = 0
    for player in players:
        if len(rooms) == 0:
            rooms.append([player[0], [player]])
        for i in range(len(rooms)):
            if len(rooms[i][1]) == m:
                continue
            if rooms[i][0] - 11 < int(player[1]) < rooms[i][0] + 11:
                rooms[i][1].append(player)


if __name__ == '__main__':
    read = sys.stdin.readline
    p, m = read().split()   # player 수, 방 정원
    players = []
    for _ in range(int(p)):
        players.append(list(read().split())) # l = [0], n = [1]
