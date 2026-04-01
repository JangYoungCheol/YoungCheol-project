# N: 동전의 종류, K: 동전 가치의 합
#동전 개수 최솟값구하기
n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# 가장 큰 동전부터 사용하기 위해 내림차순 정렬

coins.sort(reverse=True)

count = 0 # 필요한 동전 개수
# 가장 큰 동전을 가치에 넣어보고
# 동전의 가치의 합보다 동전의 금액이 크면 그 다음 작은 동전 넣기 
# 가치의 합보다 동전의 금액이 적다며 개수 1 증가 시키고 가차의 합에서 그 금액 넣기

for coin in coins:
    if k == 0: 
        break
        
    if coin <= k:
        count += k // coin 
        k %= coin          
print(count)