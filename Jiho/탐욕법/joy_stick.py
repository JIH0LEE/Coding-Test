#프로그래머스
#탐욕법
#그리디

#문제 이상함. 그리디인데 그리디 문제가 아님. 완전탐색이 맞는듯

def find_next(visited,cursor_x,cur_cursor):
    min_move=1000000
    target_cursor=0
    name_len=len(visited)
    for idx,elem in enumerate(cursor_x):
        temp_move=0
        if not visited[idx]:
            if idx<=cur_cursor:
                temp_move+=min(cur_cursor-idx,name_len-cur_cursor+idx)
            else:
                temp_move+=min(idx-cur_cursor,name_len-idx+cur_cursor)

            if temp_move<min_move:

                min_move=temp_move
                target_cursor=idx

    visited[target_cursor]=True

    return target_cursor,min_move
            

def solution(name):
    cursor_x=[]
    name_len=len(name)
    visited=[False]*name_len
    
    chr_change=0
    answer = 0
    for c in name:
        moves=ord(c)-65
        cursor_x.append(moves)
        answer+=min(moves,26-moves)
    
    for idx,elem in enumerate(cursor_x):
        if elem==0:
            visited[idx]=True
        else:
            chr_change+=1
        
    cur_cursor=0
    
    for _ in range(chr_change):
        cur_cursor,moves=find_next(visited,cursor_x,cur_cursor)
        answer+=moves
    return answer