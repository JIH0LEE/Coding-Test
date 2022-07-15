def solution(n, computers):            
    #####################어렵다########다시보기###################
    def DFS(i):
        visited[i] = 1 #visted[0] = 1 
        for a in range(n): # a= 0,1,2 
            if computers[i][a] and not visited[a]: # i번째 컴터연결배열 에서 i번째는 각각 1,2,3,4~ 와 연결된 값 [1,1,0] and not vistied[0] dfs(0)
                # visited[1] dfs[1] visited[2] dfs[2]
                DFS(a) 
                
    answer = 0 
    visited = [0 for i in range(len(computers))] #0 0 0
    for i in range(n): # 컴퓨터 3개 i = 0,1,2
        if not visited[i]: # 0:false 0:false 0:false      [0,0,0]
            DFS(i) # dfs 태움
            answer += 1 # 연결1개 더해주기
        
    return answer