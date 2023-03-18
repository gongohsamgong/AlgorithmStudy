import sys


def printRooms(m, rooms):
  for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
      print('Started!')
      # 닉네임 기준으로 정렬
      temp = sorted(rooms[i][1], key=lambda x: x[1])
      for j in range(m):
        print(temp[j][0], temp[j][1])
    else:
      print('Waiting!')
      temp = sorted(rooms[i][1], key=lambda x: x[1])
      for j in range(len(temp)):
        print(temp[j][0], temp[j][1])


def match(m, players):  # p: 플레이어 숫자, m: 방의 정원
  _rooms = []  # [10, [ [10, a], [15, b] ]] 입장기준 10인 방 하나에 플레이어 두명
  # player 인원수만큼 for문 돌아서 _room에 배치
  for player in players:
    # 방 생성 여부를 위한 flag 변수
    flag = False
    # 해당 player가 방에 배치될 수 있는지 확인하는 for문
    for i in range(len(_rooms)):
      # 방의 인원이 가득찼다면 flag 변화 혹은 append 없이 다음 방으로 넘어감
      if len(_rooms[i][1]) == m:
        continue
      # 해당 방과 레벨이 맞는 player는 append
      if int(_rooms[i][0]) - 11 < int(player[0]) < int(_rooms[i][0]) + 11:
        flag = True
        _rooms[i][1].append(player)
        break
    # flag == False라면 방에 배치되지 않았으므로, 새로운 방 생성
    if not flag:
      _rooms.append([player[0], [player]])
  # 방 정보 리턴
  return _rooms


if __name__ == '__main__':
  read = sys.stdin.readline
  p, m = map(int, read().split())  # player 수, 방 정원
  players = []
  for _ in range(p):
    players.append(list(read().split()))  # l = [0], n = [1]
  rooms = match(m, players)
  printRooms(m, rooms)
