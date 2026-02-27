# 필요 라이브러리: matplotlib
# !pip install matplotlib

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager, rc
import platform

# 한글 폰트 설정 (Windows/Mac)
if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
else:
    rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

def create_wireframe_image(filename, type='main'):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off') # 축 숨기기
    
    # 1. 브라우저/앱 헤더 그리기
    header = patches.Rectangle((0, 55), 100, 5, linewidth=1, edgecolor='#ddd', facecolor='#fff')
    ax.add_patch(header)
    ax.text(5, 56.5, "FinMatch (핀매치)", fontsize=12, fontweight='bold', color='#333')
    ax.text(70, 56.8, "INDEX   STOCK   LOGIN   JOIN", fontsize=8, color='#555')

    # 타입별 화면 구성
    if type == 'main': # 메인 화면 (3단 카드)
        # 타이틀
        ax.text(50, 48, "당신을 위한 맞춤형 금융 상품 추천", fontsize=14, fontweight='bold', ha='center')
        
        # 카드 3개 그리기
        for i in range(3):
            x_start = 10 + (i * 28)
            # 카드 박스
            card = patches.Rectangle((x_start, 15), 24, 28, linewidth=1, edgecolor='#ddd', facecolor='#fff')
            ax.add_patch(card)
            
            # 이미지 영역 (X 표시)
            img_box = patches.Rectangle((x_start+2, 28), 20, 13, facecolor='#e0e0e0')
            ax.add_patch(img_box)
            # X 그리기
            ax.plot([x_start+2, x_start+22], [28, 41], color='#fff', linewidth=2)
            ax.plot([x_start+2, x_start+22], [41, 28], color='#fff', linewidth=2)
            
            # 텍스트
            bank_names = ["국민은행", "신한은행", "우리은행"]
            products = ["KB Star 정기예금", "쏠편한 정기예금", "WON 적금"]
            rates = ["3.5%", "3.8%", "4.0%"]
            
            ax.text(x_start+2, 25, products[i], fontsize=10, fontweight='bold')
            ax.text(x_start+2, 22, f"{bank_names[i]} | 연 {rates[i]}", fontsize=9, color='#555')
            
            # 버튼
            btn = patches.Rectangle((x_start+2, 17), 20, 3, facecolor='#0066ff')
            ax.add_patch(btn)
            ax.text(x_start+12, 18.5, "상세보기", color='white', fontsize=9, ha='center', va='center')

    elif type == 'detail': # 주식 상세 화면
        # 상단 정보
        ax.text(50, 50, "삼성전자 (005930) - AI 주가 예측 분석", fontsize=14, fontweight='bold', ha='center')
        
        # 차트 영역
        chart_box = patches.Rectangle((15, 25), 70, 20, facecolor='#f9f9f9', edgecolor='#ccc')
        ax.add_patch(chart_box)
        ax.text(50, 35, "[ 주가 차트 영역 ]\n실선: 과거 데이터 / 점선: AI 예측", ha='center', color='#888')
        
        # AI 코멘트 영역
        ai_box = patches.Rectangle((15, 10), 70, 10, facecolor='#eef5ff', edgecolor='#b3d1ff')
        ax.add_patch(ai_box)
        ax.text(17, 17, "🤖 AI 분석 리포트", fontweight='bold', fontsize=10)
        ax.text(17, 14, "현재 상승 추세이며, 내일 약 1.5% 상승할 확률이 높습니다.\n매수 의견: '적극 추천'", fontsize=9)

    elif type == 'login': # 로그인 화면
        # 중앙 박스
        box = patches.Rectangle((35, 15), 30, 25, linewidth=1, edgecolor='#ddd', facecolor='#fff')
        ax.add_patch(box)
        
        # 입력 필드 1 (ID)
        input1 = patches.Rectangle((37, 32), 26, 4, linewidth=1, edgecolor='#ccc', facecolor='#fff')
        ax.add_patch(input1)
        ax.text(38, 33.5, "아이디", color='#aaa', fontsize=9)
        
        # 입력 필드 2 (PW)
        input2 = patches.Rectangle((37, 26), 26, 4, linewidth=1, edgecolor='#ccc', facecolor='#fff')
        ax.add_patch(input2)
        ax.text(38, 27.5, "비밀번호", color='#aaa', fontsize=9)
        
        # 로그인 버튼
        login_btn = patches.Rectangle((37, 20), 26, 4, facecolor='#333')
        ax.add_patch(login_btn)
        ax.text(50, 22, "Login", color='white', fontsize=10, ha='center', va='center')
        
        ax.text(50, 17, "비밀번호 찾기  |  회원가입", fontsize=8, ha='center')

    # 저장
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()
    print(f"이미지 저장 완료: {filename}")

# 이미지 3장 생성 실행
create_wireframe_image('wireframe_main.png', 'main')      # 메인 화면
create_wireframe_image('wireframe_detail.png', 'detail')  # 상세 화면
create_wireframe_image('wireframe_login.png', 'login')    # 로그인 화면