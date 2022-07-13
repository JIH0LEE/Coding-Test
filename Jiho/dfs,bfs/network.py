#프로그래머스
#dfs,bfs
#네트워크
def solution(n, computers):
    answer = 0
    visited=[False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            answer+=1
            stack=[i]
            while stack:
                comp=stack.pop()
                for idx in range(n):
                    if computers[comp][idx]==1 and not visited[idx]:
                        visited[idx]=True
                        stack.append(idx)
                
            
    return answer