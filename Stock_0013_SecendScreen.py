# 참고 : 파이썬 증권데이터 분석(김황후 저)

### p293 삼중창 매매 시스템 - 두번째 창 : 시장 파도(Market wave)
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('LG디스플레이', '2017-01-01', '2021.3.18')

ema60 = df.close.ewm(span=60).mean()        # 종가의 12주 지수 이동평균
ema130 = df.close.ewm(span=130).mean()      # 종가의 26주 지수 이동평균
macd = ema60 - ema130                       # MACD선
signal = macd.ewm(span=45).mean()           # 신호선(MACD의 9주 지수 이동평균)
macdhist = macd - signal                    # MACD 히스토그램

df = df.assign(ema130=ema130, ema60=ema60, macd=macd,
               signal=signal, macdhist=macdhist).dropna()
df['number'] = df.index.map(mdates.date2num)
ohlc = df[['number', 'open', 'high', 'low', 'close']]

ndays_high = df.high.rolling(window=14, min_periods=1).max()        # 14일 동안의 최대값
ndays_low = df.low.rolling(window=14, min_periods=1).min()          # 14일 동안의 최소값
fast_k = (df.close - ndays_low) / (ndays_high - ndays_low) * 100    # 빠른선 %K
slow_d = fast_k.rolling(window=3).mean()                            # 느린선 %D(3일 동안의 %K 평균)
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()               # %K와 %D로 데이터프레임 생성한 뒤 결측치 제거

plt.figure(figsize=(9,7))
p1 = plt.subplot(2,1,1)
plt.title('Triple Screen Trading - Second Screen (LG Display)')
plt.grid(True)
candlestick_ohlc(p1, ohlc.values, width=.6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
plt.legend(loc='best')

p2 = plt.subplot(2,1,2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['fast_k'], color='c', label='%K')
plt.plot(df.number, df['slow_d'], color='k', label='%D')
plt.yticks([0, 20, 80, 100])
plt.legend(loc='best')
plt.show()



