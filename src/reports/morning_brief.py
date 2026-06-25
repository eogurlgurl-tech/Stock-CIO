"""
Morning Brief Report Generator

Stock-CIO
"""

from datetime import datetime
from pathlib import Path

from models.market_snapshot import MarketSnapshot


class MorningBrief:
    """아침 브리핑 생성"""

    def generate(self, market: MarketSnapshot) -> Path:
        """Markdown 브리핑 생성"""

        today = datetime.now().strftime("%Y-%m-%d")

        report_dir = Path("04_REPORT/DAILY")
        report_dir.mkdir(parents=True, exist_ok=True)

        report_path = report_dir / f"{today}.md"

        report = f"""# 📈 Morning Brief

생성시간 : {datetime.now():%Y-%m-%d %H:%M:%S}

---

## 🌎 미국시장

NASDAQ : {market.nasdaq:.2f}

S&P500 : {market.sp500:.2f}

VIX : {market.vix:.2f}

---

## 🇰🇷 한국시장

KOSPI : {market.kospi:.2f}

KOSDAQ : {market.kosdaq:.2f}

---

## ⭐ 시장 평가

미국시장 : 🟢 강세

한국시장 : 🟡 중립

시장 위험도 : 🟢 낮음

---

## 🔥 오늘 주목할 섹터

1. 반도체
2. AI
3. 전력설비

---

## ⚠ 오늘 체크할 리스크

- 미국 경제지표 발표 확인
- 환율 변동성
- 기관/외국인 수급

---

## 💰 Today's Action

✅ 반도체 비중 확대 검토

✅ AI 관련주 관심 유지

✅ 현금 비중 30~40% 유지

---

## 🎯 Watch List

- ISC
- 리노공업
- 가온칩스

---

Stock-CIO v0.1 Alpha
"""

        report_path.write_text(report, encoding="utf-8")

        return report_path