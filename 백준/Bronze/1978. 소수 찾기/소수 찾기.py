N = int(input())

lst = list(map(int, input().split()))

cnt = 0

for num in lst:
    if num <= 1:
        continue

    is_prime = True

    for j in range(2, num):
        if num % j == 0:
            is_prime = False
            break
    
    if is_prime:
        cnt += 1

print(cnt)


            



