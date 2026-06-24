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

## 🤖 AI 의견

- 미국 시장 데이터 수집 완료
- 한국 시장 연결 예정
- 뉴스 분석 예정

---

Stock-CIO v0.1 Alpha
"""

        report_path.write_text(report, encoding="utf-8")

        return report_path