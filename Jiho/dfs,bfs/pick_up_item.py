from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    max_axis=100
    map=[[0 for i in range(max_axis+1)] for j in range(max_axis+1)]
    visited=[[False for i in range(max_axis+1)] for j in range(max_axis+1)]
    startX=characterX*2
    startY=characterY*2
    finalX=itemX*2
    finalY=itemY*2
    for r in rectangle:
        x1=r[0]*2
        x2=r[2]*2
        y1=r[1]*2
        y2=r[3]*2
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if map[x][y]!=2:
                    map[x][y]=1
                
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                map[x][y]=2


    
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    start=[startX,startY,0]
    queue=deque([start])
    answer = 0
    while queue:
        x,y,cost=queue.popleft()
        visited[x][y]=True
        if x==finalX and y==finalY:   
            answer=cost
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=max_axis and 0<=ny<=max_axis and map[nx][ny]==1 and not visited[nx][ny]:
                queue.append([nx,ny,cost+1])
    
    answer=answer//2
    return answer

solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
                