# 참고 : 파이썬 증권데이터 분석(김황후 저)

### Chapter6 트레이딩 전략과 구현
# p268 볼린저 밴드 구하기
# + p270 볼린저 밴드 지표(%b) 추가
# + p272 볼린저 밴드 밴드폭(bandwidth) 추가
import matplotlib.pyplot as plt
import Analyzer     # 별도 모듈

mk = Analyzer.MarketDB()
df = mk.get_daily_price('LG디스플레이', '2020-10-21', '2021.03.16')

df['MA20'] = df['close'].rolling(window=20).mean()
df['stddev'] = df['close'].rolling(window=20).std()
df['upper'] = df['MA20'] + (df['stddev'] * 2)
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# %b 추가
df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])
# 밴드폭 추가
df['bandwidth'] = (df['upper'] - df['lower']) / df['MA20'] * 100
df = df[19:]


## 볼린저 밴드 그래프
plt.figure(figsize=(9,8))
plt.subplot(2,1,1)
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
plt.plot(df.index, df['upper'], 'r--', label = 'Upper band')
plt.plot(df.index, df['MA20'], 'k--', label = 'Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label = 'Lower band')
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
plt.title('LG Display Bollinger Band (20 day, 2 std)')
plt.xticks(rotation=45)
plt.legend(loc='best')

# %b 그래프
plt.subplot(2,1,2)
plt.plot(df.index, df['PB'], color='b', label='%B')
plt.grid(True)
plt.legend(loc='best')
plt.xticks(rotation=45)
plt.show()

# 밴드폭 그래프
plt.subplot(2,1,2)
plt.plot(df.index, df['bandwidth'], color='m', label='BandWidth')
plt.grid(True)
plt.legend(loc='best')
plt.xticks(rotation=45)
plt.show()