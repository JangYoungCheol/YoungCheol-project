
N = int(input())

# 나무의 길이(초기)
tree = list(map(int, input().split()))

# 나무들이 자라는 길이 
height = list(map(int, input().split()))

# 성장속도가 빠른건 마지막에 배치해서 최대한 많은 양의 나무 획득
height.sort()

sum_tree = 0 

# 가장 많이 얻을 수 잇는 건 모든 나무를 다 베는 것이 효율적
# 초기에 자란 나무 양을 다 가져올 수 있으니
sum_tree = sum(tree)

# 일자가 지날 수로 height만큼 추가됨
for i in range(N):
    sum_tree += height[i] * i

print(sum_tree)



       
