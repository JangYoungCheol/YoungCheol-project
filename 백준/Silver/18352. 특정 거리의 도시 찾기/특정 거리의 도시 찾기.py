import sys
from collections import deque

# 입력 속도 향상을 위한 설정
input = sys.stdin.readline

# N: 도시 개수, M: 도로 개수, K: 목표 거리, X: 출발 도시
N, M, K, X = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# 도로 정보 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리를 저장할 리스트 (-1로 초기화)
distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시까지의 거리는 0

# BFS 수행
queue = deque([X])

while queue:
    now = queue.popleft()
    
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 결과 출력
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

# 최단 거리가 K인 도시가 하나도 없다면 -1 출력
if not check:
    print(-1)