package com.example.lifesaiver

import android.content.pm.PackageManager
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.core.app.ActivityCompat
import androidx.core.view.WindowCompat            // [추가]
import androidx.core.view.WindowInsetsCompat      // [추가]
import androidx.core.view.WindowInsetsControllerCompat // [추가]
import androidx.lifecycle.lifecycleScope
import com.example.lifesaiver.presentation.AppViewModel
import com.example.lifesaiver.presentation.UiEvent
import com.example.lifesaiver.ui.theme.LifesaiverTheme
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {

    private val viewModel: AppViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // [추가] 앱 실행 시 시스템 UI(상단바) 숨기기 -> 전체화면 모드
        hideSystemUI()

        // 크래시 핸들러 (앱 죽을 때 로그 표시)
        Thread.setDefaultUncaughtExceptionHandler { _, throwable ->
            val errorMsg = "오류: ${throwable.message}"
            Log.e("CRASH_HANDLER", errorMsg, throwable)
            runOnUiThread {
                Toast.makeText(applicationContext, errorMsg, Toast.LENGTH_SHORT).show()
            }
        }

        viewModel.refreshPermissions()
        if (!viewModel.uiState.value.hasPermissions) {
            requestPermissions()
        }

        setContent {
            LifesaiverTheme(darkTheme = true, dynamicColor = false) {
                val uiState by viewModel.uiState.collectAsState()

                LifesaiverApp(
                    hasPermissions = uiState.hasPermissions,
                    batteryLevel = uiState.batteryLevel,
                    isConnected = uiState.isConnected,
                    isMicOn = uiState.isMicOn,
                    isDisconnecting = uiState.isDisconnecting,

                    // 구조 신호 활성화 상태 전달
                    isRescueSignalActive = uiState.isRescueSignalActive,

                    messages = uiState.messages,
                    onRequestPermissions = { requestPermissions() },
                    onStartAutoConnect = { viewModel.onStartAutoConnect() },
                    onMicPress = { viewModel.onMicPress() },
                    onMicRelease = { viewModel.onMicRelease() },
                    onSendMessage = { text -> viewModel.onSendMessage(text) },
                    onDisconnect = { viewModel.onDisconnect() },

                    // 구조 신호 시작/중단 함수 연결
                    onStartRescueSignal = { viewModel.startRescueSignal() },
                    onStopRescueSignal = { viewModel.stopRescueSignal() }
                )
            }
        }

        // UI 이벤트(토스트) 수신
        lifecycleScope.launch {
            viewModel.uiEvents.collect { event ->
                when (event) {
                    is UiEvent.Toast -> toast(event.message)
                }
            }
        }
    }

    // [함수 추가] 상단바를 없애고 전체 화면으로 설정하는 함수
    private fun hideSystemUI() {
        // 1. 컨텐츠가 시스템 바 뒤로 그려지도록 설정 (전체 영역 사용)
        WindowCompat.setDecorFitsSystemWindows(window, false)

        // 2. 시스템 인셋 컨트롤러를 통해 상단바 숨김 처리
        WindowCompat.getInsetsController(window, window.decorView).apply {
            // 상태바(상단 시계/배터리 바) 숨기기
            hide(WindowInsetsCompat.Type.statusBars())

            // (선택사항) 네비게이션바(하단 버튼)도 숨기려면 아래 주석 해제
            // hide(WindowInsetsCompat.Type.navigationBars())

            // 화면을 쓸어내리면 잠깐 나왔다 사라지게 설정 (완전 고정)
            systemBarsBehavior = WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
        }
    }

    private fun toast(message: String) {
        runOnUiThread {
            Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
        }
    }

    private fun requestPermissions() {
        ActivityCompat.requestPermissions(this, viewModel.requiredPermissions, 1)
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode != 1) return

        val granted = grantResults.isNotEmpty() && grantResults.all {
            it == PackageManager.PERMISSION_GRANTED
        }
        viewModel.onPermissionsResult(granted)
    }
}
