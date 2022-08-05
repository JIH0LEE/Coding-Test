from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    max_axis=50
    
    map=[[-2 for i in range(max_axis+1)] for j in range(max_axis+1)]
    rectangle_idx=0
    for r in rectangle:
        rectangle_idx+=1
        for x in range(r[0],r[2]+1):
            for y in range(r[1],r[3]+1):
                if map[x][y]>=0:
                    map[x][y]=0
                elif map[x][y]==-2:
                    map[x][y]=rectangle_idx
        for x in range(r[0]+1,r[2]):
            for y in range(r[1]+1,r[3]):
                map[x][y]=-1


    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    start=[characterX,characterY,0]
    queue=deque([start])
    answer = 0
    while queue:
        x,y,cost=queue.popleft()
        if x==itemX and y==itemY:
            answer=cost
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<=max_axis and 0<=ny<=max_axis:
                if map[x][y]==0:
                    if map[nx][ny]>=0:
                        queue.append([nx,ny,cost+1])
                elif map[x][y]!=0: 
                    if map[nx][ny]==0 or map[nx][ny]==map[x][y]:
                        queue.append([nx,ny,cost+1])
                        
        
    
    return answer