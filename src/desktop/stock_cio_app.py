"""
Stock-CIO Desktop Application

Stock-CIO
"""

import io
import threading
import traceback
from contextlib import redirect_stderr, redirect_stdout
from tkinter import BOTH, DISABLED, END, NORMAL, Tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from src.core.cio_engine import CIOEngine


class StockCIOApp:
    """STOCK-CIO Windows 데스크톱 애플리케이션."""

    TRANSLATIONS = (
        ("AI Chief Investment Officer", "AI 최고투자책임자"),
        ("TODAY'S SUMMARY", "오늘의 요약"),
        ("VERY BULLISH", "매우 강세"),
        ("VERY BEARISH", "매우 약세"),
        ("STRONG BUY", "적극 매수"),
        ("BULLISH", "강세"),
        ("BEARISH", "약세"),
        ("NEUTRAL", "중립"),
        ("ACCUMULATE", "분할 매수"),
        ("DEFENSE", "방어"),
        ("REDUCE", "비중 축소"),
        ("HOLD", "유지"),
        ("SELL", "매도"),
        ("BUY", "매수"),
        ("Market Status", "시장 상태"),
        ("Recommended Action", "권고 대응"),
        ("Recommended Cash Ratio", "권고 현금 비중"),
        ("Investment", "투자 대응"),
        ("Overall Grade", "종합 등급"),
        ("Cash Ratio", "현금 비중"),
        ("Stock Ratio", "주식 비중"),
        ("MARKET DECISION", "시장 판단"),
        ("CIO SCORE", "CIO 점수"),
        ("TOTAL SCORE", "종합 점수"),
        ("GRADE", "등급"),
        ("RATING", "평가"),
        ("WATCH LIST", "관심 목록"),
        ("CIO COMMENT", "CIO 의견"),
        ("TOP NEWS", "주요 뉴스"),
        ("DATA STATUS", "데이터 수집 상태"),
        ("Analysis Time", "분석 실행시간"),
        ("Korea Market", "국내시장 데이터"),
        ("US Market", "미국시장 데이터"),
        ("UNAVAILABLE", "수집 실패"),
        ("AVAILABLE", "정상"),
        ("No Watch List", "관심 종목 없음"),
        ("No News", "수집된 뉴스 없음"),
        ("PORTFOLIO", "포트폴리오"),
        ("Positions", "보유 종목 수"),
        ("Total Asset", "총자산"),
        ("Portfolio Score", "포트폴리오 점수"),
        ("Risk Level", "위험 수준"),
        ("Decision", "판단"),
        ("Rebalance Count", "리밸런싱 대상"),
        ("FINAL DECISION", "최종 판단"),
        ("Final Action", "최종 행동"),
        ("Reason", "판단 근거"),
        ("ALLOCATION PLAN", "종목별 비중 계획"),
        ("Ticker", "종목코드"),
        ("Current", "현재 비중"),
        ("Target", "목표 비중"),
        ("Difference", "차이"),
        ("Action", "조치"),
        ("REDUCE_RISK", "위험 축소"),
        ("REBALANCE", "비중 조정"),
        ("LOW", "낮음"),
        ("MEDIUM", "보통"),
        ("HIGH", "높음"),
        ("Version", "버전"),
        ("Started", "시작 시간"),
        ("Initialize System", "시스템 초기화"),
        ("Load Market Data", "시장 데이터 수집"),
        ("Market Analyze", "시장 분석"),
        ("Score Calculate", "종합점수 계산"),
        ("Market Decision", "시장 판단"),
        ("Portfolio Pipeline", "포트폴리오 분석"),
        ("[7/8] Dashboard", "[7/8] 대시보드"),
        ("Morning Brief", "모닝브리프"),
        ("Report Saved", "보고서 저장"),
        ("System Ready", "시스템 준비 완료"),
        ("System Context", "시스템 처리 결과"),
        ("STATUS", "상태"),
        ("ACTION", "대응"),
        ("CASH", "현금"),
        ("STOCK", "주식"),
    )

    def __init__(self, root: Tk) -> None:
        """한글 데스크톱 화면을 구성한다."""

        self._root = root
        self._root.title("STOCK-CIO 투자 대시보드")
        self._root.geometry("920x720")
        self._root.minsize(760, 560)

        self._status = ttk.Label(
            root,
            text="분석 준비 완료",
        )
        self._status.pack(padx=12, pady=(12, 4), anchor="w")

        self._run_button = ttk.Button(
            root,
            text="분석 실행",
            command=self._start_analysis,
        )
        self._run_button.pack(padx=12, pady=4, anchor="w")

        self._output = ScrolledText(
            root,
            wrap="word",
            font=("Malgun Gothic", 10),
        )
        self._output.pack(
            fill=BOTH,
            expand=True,
            padx=12,
            pady=(4, 12),
        )
        self._output.insert(
            END,
            "'분석 실행' 버튼을 누르면 최신 분석을 시작합니다.\n",
        )
        self._output.configure(state=DISABLED)

    def _start_analysis(self) -> None:
        """화면을 멈추지 않고 분석을 시작한다."""

        self._run_button.configure(state=DISABLED)
        self._status.configure(text="데이터 수집 및 분석 진행 중...")

        worker = threading.Thread(
            target=self._execute_analysis,
            daemon=True,
        )
        worker.start()

    def _execute_analysis(self) -> None:
        """CIOEngine을 실행하고 출력 내용을 수집한다."""

        output = io.StringIO()
        succeeded = True

        try:
            with redirect_stdout(output), redirect_stderr(output):
                CIOEngine().run()
        except Exception:
            succeeded = False
            traceback.print_exc(file=output)

        self._root.after(
            0,
            self._finish_analysis,
            self._translate_output(output.getvalue()),
            succeeded,
        )

    def _finish_analysis(
        self,
        output: str,
        succeeded: bool,
    ) -> None:
        """분석 결과를 화면에 표시한다."""

        self._output.configure(state=NORMAL)
        self._output.delete("1.0", END)
        self._output.insert(END, output)
        self._output.configure(state=DISABLED)
        self._output.see(END)

        self._status.configure(
            text=(
                "분석 완료"
                if succeeded
                else "분석 실패 - 아래 오류 내용을 확인하세요"
            )
        )
        self._run_button.configure(state=NORMAL)

    @classmethod
    def _translate_output(cls, output: str) -> str:
        """분석 결과의 사용자 표시 문구를 한글로 변환한다."""

        translated = cls._remove_internal_context(output)

        for source, target in cls.TRANSLATIONS:
            translated = translated.replace(source, target)

        return translated

    @staticmethod
    def _remove_internal_context(output: str) -> str:
        """사용자에게 불필요한 내부 Context 목록을 제거한다."""

        marker_index = output.find("System Context")

        if marker_index < 0:
            return output

        separator = "=" * 60
        section_start = output.rfind(
            separator,
            0,
            marker_index,
        )

        if section_start < 0:
            section_start = marker_index

        return output[:section_start].rstrip() + "\n"
