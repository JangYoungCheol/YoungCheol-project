import sys
from collections import deque

# 상하좌우 이동을 위한 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문한 곳은 0으로 바꿔 다시 방문하지 않도록 함
    count = 1
    
    while queue:
        curr_x, curr_y = queue.popleft()
        
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            
            # 지도 범위를 벗어나지 않고, 집이 있는 경우(1)
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                count += 1
    return count

# 입력 처리
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

complexes = []

# 지도 전체를 순회하며 집이 있는 곳을 찾음
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # 새로운 단지를 발견하면 BFS 시작
            complexes.append(bfs(i, j))

# 결과 출력
complexes.sort()  # 오름차순 정렬
print(len(complexes))  # 총 단지 수
for count in complexes:
    print(count)