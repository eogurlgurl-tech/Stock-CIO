from collectors.yahoo_loader import YahooLoader

loader = YahooLoader()

market = loader.load()

print("=" * 50)

print("Yahoo Loader Test")

print("=" * 50)

print(f"KOSPI  : {market.kospi}")
print(f"KOSDAQ : {market.kosdaq}")
print(f"NASDAQ : {market.nasdaq}")
print(f"S&P500 : {market.sp500}")
print(f"VIX    : {market.vix}")