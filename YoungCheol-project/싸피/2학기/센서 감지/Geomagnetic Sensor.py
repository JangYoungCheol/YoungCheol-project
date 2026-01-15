import subprocess
import os
import time

# ⚠️ 본인의 adb.exe 경로 (기존 경로 유지)
ADB_PATH = r"C:\Users\SSAFY\Desktop\장영철\센서\platform-tools\adb.exe"

def monitor_geomagnetic():
    print("지자기 센서 데이터 수신 대기 중...", end="\r")
    
    while True:
        try:
            # 1. dumpsys 명령어로 센서 데이터 스냅샷 가져오기
            cmd = f'"{ADB_PATH}" shell dumpsys sensorservice'
            res = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')
            lines = res.split('\n')
            
            # 화면 지우기
            os.system('cls') 
            
            print("="*50)
            print("   🧭 갤럭시 지자기 센서(Magnetometer) 실시간 감시")
            print("="*50)

            found = False
            
            # 2. 파싱 로직
            for i, line in enumerate(lines):
                # [수정] 가속도 대신 'Magnetometer' 또는 'Magnetic'을 찾습니다.
                # 보통 'AK09918 Magnetometer' 등의 이름으로 나옵니다.
                if "Magnetometer" in line or "Magnetic Field" in line:
                    # 센서 목록의 헤더인지 확인 (핸들 값 0x... 포함 여부)
                    if "0x" in line:
                        print(f"📡 센서 감지됨: {line.strip()}")
                        
                        # 'last 50 events' 섹션 찾기
                        for j in range(i, i + 20):
                            if j < len(lines) and "last" in lines[j] and "events" in lines[j]:
                                try:
                                    # 최신 데이터 줄 가져오기
                                    if j+1 < len(lines):
                                        data_row = lines[j+1].strip()
                                        print(f"\n🧲 최신 Raw 데이터 (x, y, z) [µT]:")
                                        print(f"   👉 {data_row}")
                                        found = True
                                except IndexError:
                                    pass
                                break
                        
                    if found: break 

            if not found:
                print("\n❌ 지자기 센서를 찾을 수 없습니다.")
                print("1. 휴대폰 화면이 켜져 있나요?")
                print("2. 지도 앱이나 나침반 앱을 실행하면 데이터가 더 잘 나옵니다.")
        
        except subprocess.CalledProcessError:
            print("\n❌ ADB 연결 끊김. 케이블을 확인하세요.")
            break
        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")
            break
        
        # 갱신 주기
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_geomagnetic()