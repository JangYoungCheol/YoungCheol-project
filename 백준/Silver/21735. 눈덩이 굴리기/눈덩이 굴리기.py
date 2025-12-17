#앞마당의 길이는 N이고 위치는 1부터 N까지
# 위치 i에 눈이 ai 만큼 쌓여있다 
# M초동안 굴려서 눈사람 제작
# 시작 크기는 1 시작 위치는  0

n, m = map(int, input().split())
snows = list(map(int, input().split()))

ans = 0

def dfs(idx, time, size):
    global ans
    
    # 매 순간 최댓값 갱신
    ans = max(ans, size)
    
    # 시간이 다 됐거나, 마지막 위치에 도달/초과했다면 종료
    # 주의: 문제에서 "끝에 도달한 경우 남은 시간과 관계없이 끝"이라고 했음
    # idx가 n보다 크거나 같으면 범위를 벗어나거나 끝에 닿은 것 (0-based index 기준 idx >= n이면 종료라고 가정 등 범위 체크 필요)
    if time == m:
        return
    
    # 1. 굴리기 (현재 위치 idx에서 +1 칸 이동 -> snows[idx])
    # 현재 위치가 start(0)이라면 다음 칸은 첫 번째 눈(snows[0])
    # 위치 계산: 현재 위치를 idx라고 할 때, 
    # 초기 시작 위치를 -1 또는 별도 처리 해야함. 
    # 편의상: idx를 '다음에 밟을 배열의 인덱스'로 생각하면 편함
    
    # Case 1: 굴리기 (+1칸)
    if idx < n:
        dfs(idx + 1, time + 1, size + snows[idx])
        
    # Case 2: 던지기 (+2칸)
    if idx + 1 < n:
        dfs(idx + 2, time + 1, (size // 2) + snows[idx + 1])

# 초기 시작: 다음 밟을 인덱스 0, 시간 0, 크기 1
dfs(0, 0, 1)
print(ans)