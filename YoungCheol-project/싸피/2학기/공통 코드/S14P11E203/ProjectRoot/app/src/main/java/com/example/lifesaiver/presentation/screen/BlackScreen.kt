package com.example.lifesaiver.presentation.screen

import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.delay
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

@Composable
fun BlackSaverScreen(
    batteryLevel: Int,
    onUnlock: () -> Unit
) {
    var currentTime by remember { mutableStateOf("") }

    LaunchedEffect(Unit) {
        val formatter = SimpleDateFormat("HH:mm", Locale.getDefault())
        while (true) {
            currentTime = formatter.format(Date())
            delay(1000L)
        }
    }

    val batteryColor = if (batteryLevel <= 20) Color.Red else Color.Green

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(Color.Black)
            .pointerInput(Unit) {
                detectTapGestures(
                    onDoubleTap = { onUnlock() }
                )
            },
        contentAlignment = Alignment.Center
    ) {
        Column(
            modifier = Modifier.fillMaxWidth(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // 1. 현재 시간 (앱 기본 폰트 사용 -> 통일성 확보)
            Text(
                text = currentTime,
                color = Color.White,
                fontSize = 80.sp,              // 시원하게 큰 사이즈
                fontWeight = FontWeight.Thin,  // [핵심] 얇은 두께로 세련됨 + 기본 폰트 사용
                textAlign = TextAlign.Center,
                // fontFamily = FontFamily.Monospace (삭제함: 기본 폰트로 돌아감)
                letterSpacing = (-2).sp        // 글자 간격을 살짝 좁혀서 단단한 느낌
            )

            Spacer(modifier = Modifier.height(12.dp))

            // 2. 배터리 정보
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.Center,
                verticalAlignment = Alignment.CenterVertically
            ) {
                Text(
                    text = "🔋",
                    fontSize = 22.sp,
                    textAlign = TextAlign.Center
                )
                Spacer(modifier = Modifier.width(6.dp))
                Text(
                    text = "$batteryLevel%",
                    color = batteryColor,
                    fontSize = 22.sp,
                    fontWeight = FontWeight.Normal, // 기본 두께
                    // fontFamily = FontFamily.Monospace (삭제함)
                    textAlign = TextAlign.Center
                )
            }

            Spacer(modifier = Modifier.height(60.dp))

            // 3. 상태 메시지 (기본 폰트)
            Text(
                text = "절전 모드 작동 중",
                color = Color.Gray,
                fontSize = 16.sp,
                fontWeight = FontWeight.Medium,
                textAlign = TextAlign.Center
            )
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = "구조 신호를 계속 보내고 있습니다",
                color = Color.DarkGray,
                fontSize = 13.sp,
                textAlign = TextAlign.Center
            )
        }

        // 하단 안내 문구
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(bottom = 60.dp),
            contentAlignment = Alignment.BottomCenter
        ) {
            Text(
                text = "화면을 두 번 두드리면 켜집니다",
                color = Color.DarkGray.copy(alpha = 0.6f),
                fontSize = 14.sp,
                textAlign = TextAlign.Center
            )
        }
    }
}
