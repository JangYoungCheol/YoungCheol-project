# 친구와 친구 초대 

# 1인 상근이 본인
# 인접리스트 
n = int(input()) # 동기 수
m = int(input()) # 리스트 길이
adj = [[] for _ in range(n + 1)]

# 1. 인접 리스트 채우기
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

invite = set()

# 2. 상근이(1번)의 친구와 친구의 친구 탐색
if adj[1]: # 상근이의 친구가 있을 때만 탐색
    for friend in adj[1]:
        invite.add(friend) # 친구 추가
        
        for f_of_friend in adj[friend]:
            if f_of_friend != 1: # 상근이 본인은 제외
                invite.add(f_of_friend) # 친구의 친구 추가

# 3. 초대할 사람의 수 출력
print(len(invite))