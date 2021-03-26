# 참고 : 파이썬 증권데이터 분석(김황후 저)

# p358 백트레이더 설치
# pip install backtrader
# p360 RSI를 이용한 단순 백테스트
# 참고 : https://jonghyunho.github.io/data/analysis/Backtrader-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%94%A9-%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98.html
# 참고 : https://randlow.github.io/posts/trading/trading-indicators-backtrader/
from datetime import datetime
import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data.close)
    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

cerebro = bt.Cerebro()      # Cerobro 클래스 : backtrader의 클래스
cerebro.addstrategy(MyStrategy)
data = bt.feeds.YahooFinanceData(dataname='034220.KS',
                                 fromdate=datetime(2017,1,1),
                                 todate=datetime(2021,3,26))
cerebro.adddata(data)
cerebro.broker.setcash(10000000)
cerebro.addsizer(bt.sizers.SizerFix, stake=30)

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()
print(f'Final Portfolio Value   : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot()


