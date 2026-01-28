# 매일 알람을 45분 일찍 알람설정


H, M = map(int, input().split())

#H : 시
#M : 분

if M < 45:
    M += 15

    if H == 0 :
        H = 23
    else:
        H -= 1
else:
    M -= 45

print (H, M)
