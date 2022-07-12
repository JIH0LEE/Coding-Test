# DFS(Depth-First Search) 깊이 우선 탐색: 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
# 자기 자신을 호출하는 순환 알고리즘의 형태
# 어떤 노드를 방문했었는지 여부를 반드시 검사해야함
# DFS를 구현하는 두가지 방법
# 1. 스택을 사용한 DFS
# 2. 재귀를 이용한 DFS

from tkinter import N


graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 재귀를 이용한 DFS


def dfs_recursive(graph, start, visited=[]):
    # 데이터 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

# Deque를 활용한 DFS


def dfs_deque(graph, start_node):
    from collections import deque
    visited = []
    need_visited = deque()

    # 시작 노드를 설정
    need_visited.append(start_node)

    # 방문이 필요한 리스트가 존재한다면
    while need_visited:
        # 마지막 노드를 가져오고
        node = need_visited.pop()

        # 만약 리스트에 없다면
        if node not in visited:

            # 방문 리스트에 노드를 추가
            visited.append(node)

            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited

# 스택을 활용한 DFS


def dfs_stack(graph, start_node):
    # 2개의 리스트를 별도로 관리
    need_visited, visited = list(), list()

    # 시작노드 지정하기
    need_visited.append(start_node)

    # 만약 아직도 방문이 필요한 노드가 있다면
    while need_visited:
        # 그 중에서 가장 마지막 데이터 추출
        node = need_visited.pop()
        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:

            # 방문한 목록에 추가
            visited.append(node)

            # 그 노드에 연결된 노드로 이동(연결된 노드를 추가)
            need_visited.extend(graph[node])

    return visited
