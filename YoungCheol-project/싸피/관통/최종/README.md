# 💸 FinMatch (핀매치)
### 금융을 쉽고 친근하게, 내 손안의 자산 파트너
> **SSAFY 13기 1학기 관통 프로젝트 (2인 풀스택 집중 개발)**

---

## 📖 1. 프로젝트 개요 (Overview)

> **"복잡한 금융 상품, 지도와 알고리즘으로 한눈에."**

**FinMatch**는 사회초년생들이 자신의 성향에 맞는 예·적금 상품을 추천받고, 근처 은행 영업점을 손쉽게 찾을 수 있는 **금융 플랫폼**입니다.
통상적인 팀 규모보다 적은 **2인 1팀(Pair Project)** 체제로 진행되었으며, 기획부터 DB 설계, API 구현, UI 디자인까지 **Full Stack**으로 개발하여 완성도 높은 로컬 서비스를 구현했습니다.

- **📅 개발 기간**: 2025.11 ~ 2025.12 (약 1개월)
- **👥 팀 구성**: 2인 (Full Stack)
- **💻 개발 환경**: Localhost (Frontend: `Port 5173` / Backend: `Port 8000`)

<br/>

## 👨‍💻 2. 담당 역할 (My Roles)

> **"프론트와 백엔드의 경계 없이, 서비스의 A to Z를 주도했습니다."**

| 영역 | 상세 기여 내용 |
|:---:|:---|
| **Front-end** | • **Vue.js 3 & Pinia** 기반 SPA 구조 설계 및 컴포넌트 개발<br/>• **Kakao Map API** 연동 및 커스텀 오버레이(길찾기, 상세정보) 구현<br/>• **Chart.js**를 활용한 환율 변동 추이 시각화 |
| **Back-end** | • **Django REST Framework** 기반 RESTful API 설계<br/>• 금융감독원 데이터 전처리 및 **개인화 추천 알고리즘** 로직 구현<br/>• User-Product-Bank 간의 **ERD(관계형 데이터)** 설계 |
| **Collaboration** | • **Git Flow** 전략 수립 및 충돌 방지를 위한 기능별 브랜치 관리<br/>• **Notion**을 활용한 API 명세서 작성 및 일정 관리 |

<br/>

## 🛠️ 3. 기술 스택 (Tech Stack)

| 구분 | 기술 (Technology) | 선정 이유 |
|:---:|:---|:---|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) | 금융 데이터 처리에 강한 Python과 웹 표준 JS 사용 |
| **Frontend** | ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white) ![Pinia](https://img.shields.io/badge/Pinia-FFD11B?style=flat-square&logo=pinia&logoColor=black) ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white) | 빠른 생산성과 직관적인 전역 상태 관리(Pinia)를 위해 채택 |
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | 강력한 ORM 기능과 데이터 분석 라이브러리(Pandas) 활용 용이 |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) | 로컬 개발 환경에서의 빠른 설정과 테스트 용이성 |
| **API** | **Kakao Map API**, **한국수출입은행 API** | 위치 기반 시각화 및 실시간 환율 정보 제공 |

<br/>

## 💡 4. 핵심 기능 (Key Features)

### ① 🗺️ 내 주변 은행 찾기 (Smart Map)
- **기능**: 사용자의 현재 위치 또는 검색 지역 **반경 1km 내의 은행 지점**을 마커로 표시.
- **특징**: 단순 위치 표시를 넘어, **영업점 상세 정보와 길 찾기 기능**을 연동하여 O2O(Online to Offline) 경험 제공.
- **기술**: `Kakao Map API`의 **Clusterer**를 활용해 지도 줌 레벨에 따른 마커 그룹화 구현.

### ② 💰 맞춤형 상품 추천 (Algorithm)
- **기능**: 나이, 자산, 연봉, 투자 성향(설문)을 분석하여 **최적의 예·적금 상품 Top 3** 추천.
- **로직**:
    1. 금융감독원 API 데이터 파싱 및 DB 적재 (우대 금리, 가입 제한 등 데이터 전처리).
    2. **사용자 프로필 벡터**와 **상품 속성** 간의 가중치 매칭 알고리즘 적용.

### ③ 📉 실시간 환율 계산기
- **기능**: 주요 통화(USD, JPY, EUR 등)의 실시간 매매 기준율 조회 및 원화 환산 계산 제공.
- **UI**: 최근 1주일간의 환율 변동 폭을 **그래프(Chart.js)**로 시각화하여 정보 전달력 강화.

<br/>

## 🚀 5. 트러블 슈팅 (Troubleshooting)

> "배포 전 단계인 로컬 개발 환경에서의 이슈를 집요하게 파고들어 해결했습니다."

### 🔥 Issue 1: Kakao Map API 로컬 연동 오류
- **문제 상황**: 로컬 서버(`localhost`)에서 지도를 호출하자 `APP_KEY` 인증 오류 및 백지 화면 현상 발생.
- **원인 분석**: 카카오 개발자 콘솔에 등록된 도메인 포트(`8080`)와 실제 Vite 실행 포트(`5173`) 불일치, 그리고 스크립트 로드 타이밍 문제.
- **해결**:
    1. Kakao Developers 플랫폼 설정에 `http://localhost:5173`을 정확히 등록.
    2. `.env` 파일을 생성하여 API 키를 분리.
    3. Vue의 `onMounted` 훅 내부에서 비동기로 스크립트를 로드하도록 리팩토링하여 **렌더링 안정성 확보**.

### 🔥 Issue 2: 프론트-백엔드 통신 간 CORS 에러
- **문제 상황**: Vue(`:5173`)에서 Django(`:8000`)로 로그인 요청 시 **CORS 정책 위반 에러** 발생.
- **해결**:
    1. Django에 `django-cors-headers` 라이브러리 설치.
    2. `settings.py`의 `CORS_ALLOWED_ORIGINS` 리스트에 **프론트엔드 로컬 주소를 명시적으로 허용**하여 보안과 통신 문제 해결.

<br/>

## 🏁 6. 프로젝트 실행 방법 (How to Run)

이 프로젝트는 **로컬 환경**에서 실행되도록 설정되어 있습니다.

### Backend (Django)
```bash
$ cd backend
$ python -m venv venv              # 가상환경 생성
$ source venv/Scripts/activate     # (Windows: venv\Scripts\activate)
$ pip install -r requirements.txt  # 의존성 설치
$ python manage.py migrate         # DB 마이그레이션
$ python manage.py runserver       # 서버 실행
# Server running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```

### Frontend (Vue.js)
```bash
$ cd frontend
$ npm install                        # Node 모듈 설치
$ npm run dev                        # 개발 서버 실행
# App running on http://localhost:5173/
```


### 📝 7. 회고 (Retrospective)

### 🌟 2인 풀스택 개발을 통해 배운 점

4~5인 팀 프로젝트였다면 백엔드나 프론트엔드 중 한 분야만 깊게 팠겠지만, 2인 프로젝트였기에 데이터베이스 설계부터 화면 렌더링까지 서비스의 전체 흐름(Data Flow)을 완벽하게 이해할 수 있었습니다.

특히, API 명세서가 단순한 문서가 아니라 프론트엔드와 백엔드를 잇는 가장 중요한 약속임을 깨달았습니다. 초기에는 구두로 소통하다가 데이터 타입 불일치 오류를 겪은 후, Notion과 Postman을 활용해 명세를 꼼꼼히 관리하는 습관을 들이게 되었습니다.

### 🔧 아쉬웠던 점 및 향후 계획

배포까지 진행하지 못해 실제 사용자 트래픽을 받아보지 못한 점이 아쉽습니다. 하지만 로컬 환경에서 CORS나 API Key 환경변수 관리 등 실제 운영 환경과 유사한 문제들을 겪으며 기초 체력을 길렀습니다. 향후 Docker를 활용한 컨테이너화와 AWS EC2 배포를 통해 서비스를 온라인에 런칭하는 것이 다음 목표입니다.