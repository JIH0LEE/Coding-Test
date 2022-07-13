#프로그래머스
#dfs,bfs
#게임 맵 최단거리
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue=deque([(1,0,0)])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    answer = -1
    is_finish=False
    while queue:
        distance,x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]:
                if (nx, ny) == (n-1, m-1):
                    answer=distance+1
                    is_finish=True
                    break
                queue.append((distance+1,nx, ny))
                visited[nx][ny] = True
        if is_finish:
            break
    return answer