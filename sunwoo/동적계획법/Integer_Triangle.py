def solution(triangle):
    height = len(triangle)
    
    # Top-down 방법
    for i in range(1, height):
        for j in range(i+1):
            print(i, j)
            if j == 0: # 가장 왼쪽의 경우 왼쪽수를 모두 더하면서 내려감
                triangle[i][j] += triangle[i-1][j]
            elif j == i:  # 가장 오른쪽의 경우 오른쪽수를 모두 더하면서 내려감
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]) # 그외의 경우 윗단계의 두 수중 큰 값을 더하면서 내려감
    
    answer = max(triangle[-1])
    return answer
  
  
  
  
  
  
  # Bottom-Up 방법
  def solution(triangle):
    height = len(triangle)
    
    for i in range(height-1, 0, -1):
        for j in range(i):
            # 바로 윗 단계에서의 최댓값은, 아랫단계 두개중 큰 값과 더한 값이다.
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
            
    answer = triangle[0][0]
    return answer
  
  
  
  
  '''
  
  바로 윗단계의 최댓값을 하나 아래에 위치한 두 값중 큰 값과 더한 값으로 갱신해나가면서 꼭대기까지 올라가면 문제를 해결할 수 있다.
  
  해당 문제에서는 내려가는 3가지의 방법이 존재한다.

  가장 왼쪽라인만 더하면서 내려가는 경우
  가장 오른쪽라인만 더하면서 내려가는 경우
  나머지 라인의 경우 더 큰값을 고르면서 내려가는 경우
  먼저, 앞의 2가지의 경우는 최댓값을 고를 필요가 없으므로 고정되어있다. 가운데 라인의 경우는 아래 존재하는 두개의 수들중 큰 값을 더하면서 내려가면 된다.

  최종적으로 가장 마지막 라인중 최댓값을 출력하면 문제를 해결 can
  '''
