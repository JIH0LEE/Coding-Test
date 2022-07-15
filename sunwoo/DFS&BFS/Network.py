def dfs(x,computers):
    computers[x][x]=2 #들린거 표시
    for i in range(len(computers[x])):
        if computers[x][i]==1 and computers[i][i]!=2: # 처음 들리는 곳이면
            dfs(i,computers)
    
    
def solution(n, computers):
    answer = 0
 
    
    for i in range(n):
        if computers[i][i]==1: #처음 들리는 곳
            dfs(i,computers)
            answer+=1
    return answer
  
  
  
  '''
  dfs로 풀기
  '''
