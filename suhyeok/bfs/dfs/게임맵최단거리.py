from collections import deque


def bfs(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque([(0, 0)])
    dist = [[-1]*len(maps[0]) for _ in range(len(maps))]
    dist[0][0] = 1
    while queue:
        current_x, current_y = queue.popleft()
        for direction in range(4):  # 동서남북
            loc_x, loc_y = current_x+dx[direction], current_y+dy[direction]
            if 0 <= loc_x < len(maps) and 0 <= loc_y < len(maps[0]):
                if dist[loc_x][loc_y] == -1 and maps[loc_x][loc_y] == 1:
                    dist[loc_x][loc_y] = dist[current_x][current_y]+1
                    queue.append((loc_x, loc_y))
    return dist[-1][-1]


def solution(maps):
    answer = 0
    # bfs로 풀자
    print(len(maps))
    answer = bfs(maps)

    return answer
